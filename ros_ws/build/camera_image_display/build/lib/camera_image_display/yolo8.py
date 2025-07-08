import cv2
import numpy as np
import sys
import time
from collections import deque
# 将 rknnlite 的路径添加到 sys.path 中
sys.path.append('/home/elf/miniconda3/envs/yolo/lib/python3.10/site-packages')
from rknnlite.api import RKNNLite
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# 假设的类别列表，需根据你的模型实际情况修改
CLASSES = ['cat', 'dog']

# 设置对象置信度阈值和非极大值抑制(NMS)阈值
OBJ_THRESH = 0.25
NMS_THRESH = 0.45
IMG_SIZE = (640, 640)


def filter_boxes(boxes, box_confidences, box_class_probs):
    # 筛选出满足条件的框，根据置信度和类别概率筛选出有效的框
    box_confidences = box_confidences.reshape(-1)
    class_max_score = np.max(box_class_probs, axis=-1)
    classes = np.argmax(box_class_probs, axis=-1)
    _class_pos = np.where(class_max_score * box_confidences >= OBJ_THRESH)
    scores = (class_max_score * box_confidences)[_class_pos]
    boxes = boxes[_class_pos]
    classes = classes[_class_pos]
    return boxes, classes, scores


def nms_boxes(boxes, scores):
    # 使用非极大值抑制(NMS)来消除冗余框，保留最优的检测框
    x = boxes[:, 0]
    y = boxes[:, 1]
    w = boxes[:, 2] - boxes[:, 0]
    h = boxes[:, 3] - boxes[:, 1]
    areas = w * h
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x[i], x[order[1:]])
        yy1 = np.maximum(y[i], y[order[1:]])
        xx2 = np.minimum(x[i] + w[i], x[order[1:]] + w[order[1:]])
        yy2 = np.minimum(y[i] + h[i], y[order[1:]] + h[order[1:]])
        w1 = np.maximum(0.0, xx2 - xx1 + 0.00001)
        h1 = np.maximum(0.0, yy2 - yy1 + 0.00001)
        inter = w1 * h1
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        inds = np.where(ovr <= NMS_THRESH)[0]
        order = order[inds + 1]
    keep = np.array(keep)
    return keep


def box_process(position):
    # 处理边界框的坐标，将其转换为实际图像上的坐标
    grid_h, grid_w = position.shape[2:4]
    col, row = np.meshgrid(np.arange(0, grid_w), np.arange(0, grid_h))
    col = col.reshape(1, 1, grid_h, grid_w)
    row = row.reshape(1, 1, grid_h, grid_w)
    grid = np.concatenate((col, row), axis=1)
    stride = np.array([IMG_SIZE[1] // grid_h, IMG_SIZE[0] // grid_w]).reshape(1, 2, 1, 1)
    # 这里假设dfl函数和文章中功能一致，若有差异需调整
    # 暂时按照文章实现
    n, c, h, w = position.shape
    p_num = 4
    mc = c // p_num
    y = position.reshape(n, p_num, mc, h, w)
    max_val = np.max(y, axis=2, keepdims=True).repeat(mc, axis=2)
    exps = np.exp(y - max_val)
    y = exps / np.sum(exps, axis=2, keepdims=True)
    acc_metrix = np.arange(mc).reshape(1, 1, mc, 1, 1)
    y = (y * acc_metrix).sum(2)
    box_xy = grid + 0.5 - y[:, 0:2, :, :]
    box_xy2 = grid + 0.5 + y[:, 2:4, :, :]
    xyxy = np.concatenate((box_xy * stride, box_xy2 * stride), axis=1)
    return xyxy


def yolov8_post_process(input_data):
    # 模型输出的原始预测结果经过后处理，以生成最终的检测结果
    boxes, scores, classes_conf = [], [], []
    default_branch = 3
    pair_per_branch = len(input_data) // default_branch
    # 处理每个分支数据
    for i in range(default_branch):
        boxes.append(box_process(input_data[pair_per_branch * i]))
        classes_conf.append(input_data[pair_per_branch * i + 1])
        scores.append(np.ones_like(input_data[pair_per_branch * i + 1][:, :1, :, :], dtype=np.float32))

    # 将输入张量 _in 重新排列并展平
    def sp_flatten(_in):
        ch = _in.shape[1]
        _in = _in.transpose(0, 2, 3, 1)
        return _in.reshape(-1, ch)

    # 使用sp_flatten函数展平每个分支的boxes、classes_conf和scores
    boxes = [sp_flatten(_v) for _v in boxes]
    classes_conf = [sp_flatten(_v) for _v in classes_conf]
    scores = [sp_flatten(_v) for _v in scores]

    # 将每个分支的展平数据连接成一个整体
    boxes = np.concatenate(boxes)
    scores = np.concatenate(scores)
    classes_conf = np.concatenate(classes_conf)

    # 过滤框
    boxes, classes, scores = filter_boxes(boxes, scores, classes_conf)

    # nms--非极大值抑制
    nboxes, nclasses, nscores = [], [], []
    for c in set(classes):
        inds = np.where(classes == c)
        b = boxes[inds]
        c = classes[inds]
        s = scores[inds]
        keep = nms_boxes(b, s)
        if len(keep) != 0:
            nboxes.append(b[keep])
            nclasses.append(c[keep])
            nscores.append(s[keep])

    if not nclasses and not nscores:
        return None, None, None
    boxes = np.concatenate(nboxes)
    classes = np.concatenate(nclasses)
    scores = np.concatenate(nscores)
    return boxes, classes, scores


def draw(image, boxes, scores, classes, fps=None):
    # 画框
    for box, score, cl in zip(boxes, scores, classes):
        top, left, right, bottom = [int(_b) for _b in box]
        cv2.rectangle(image, (top, left), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image, '{0} {1:.2f}'.format(CLASSES[cl], score),
                    (top, left - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # 显示帧率
    if fps is not None:
        cv2.putText(image, f"FPS: {fps:.2f}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return image


class YoloInferenceNode(Node):
    def __init__(self, model_path):
        super().__init__("yolo_inference_node")
        self.model = Model(model_path)
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(
            Image,
            "/ascamera/camera_publisher/rgb0/image",  # ROS 2图像话题
            self.image_callback,
            10
        )
        
        # 帧率计算相关变量
        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0.0
        self.fps_deque = deque(maxlen=30)  # 存储最近30帧的处理时间

    def image_callback(self, msg):
        try:
            # 记录开始处理时间
            frame_start_time = time.time()
            
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            yolo_result = self.model.inference(cv_image)
            if yolo_result:
                boxes, classes, scores = yolov8_post_process(yolo_result)
                if boxes is not None:
                    # 计算帧率
                    self.frame_count += 1
                    current_time = time.time()
                    elapsed_time = current_time - self.start_time
                    
                    # 每10帧更新一次显示的帧率，减少计算开销
                    if self.frame_count % 10 == 0:
                        self.fps = self.frame_count / elapsed_time
                    
                    # 计算处理一帧的时间并添加到队列
                    process_time = current_time - frame_start_time
                    self.fps_deque.append(process_time)
                    
                    # 使用队列中的平均处理时间计算平滑的FPS
                    avg_process_time = sum(self.fps_deque) / len(self.fps_deque)
                    smooth_fps = 1.0 / avg_process_time if avg_process_time > 0 else 0
                    
                    result_image = draw(cv_image, boxes, scores, classes, smooth_fps)
                    cv2.imshow('Detection Result', result_image)
                    cv2.waitKey(1)
                    
        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")


class Model:
    def __init__(self, model_path):
        self.rknn_model = model_path
        self.rknn_lite = RKNNLite()
        print(f'--> Load {self.rknn_model} model')
        ret = self.rknn_lite.load_rknn(self.rknn_model)
        if ret != 0:
            print('Load RKNNLite model failed')
            exit(ret)
        print('done')
        # 初始化运行环境
        print('--> Init runtime environment')
        ret = self.rknn_lite.init_runtime()
        if ret != 0:
            print('Init runtime environment failed')
            exit(ret)
        print('done')

    def inference(self, img_src):
        if img_src is None:
            print('Error: image read failed')
            return None
        img = cv2.resize(img_src, IMG_SIZE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.expand_dims(img, 0)
        # 修正这里的参数名
        outputs = self.rknn_lite.inference(inputs=[img])
        return outputs

    def release(self):
        self.rknn_lite.release()


def main():
    import rclpy
    yolo_model_path = '/home/elf/ros_ws/src/camera_image_display/camera_image_display/yolov8.rknn'
    rclpy.init()
    node = YoloInferenceNode(yolo_model_path)
    rclpy.spin(node)
    node.model.release()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()    
