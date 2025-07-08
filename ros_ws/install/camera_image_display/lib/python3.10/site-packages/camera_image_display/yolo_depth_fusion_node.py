# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import time
import message_filters # 用于同步图像话题
import serial  # 引入串口通信库
import serial.tools.list_ports


# 尝试从 yolo8.py 脚本中导入必要的函数
# 这样可以避免代码重复，并保持代码的模块化
try:
    from .yolo8 import yolov8_post_process, draw, Model, CLASSES, IMG_SIZE
except ImportError:
    print("错误：无法从 yolo8.py 导入函数。请确保 yolo8.py 文件在同一个目录下。")
    print("将使用此文件内的备份函数。")
    # 如果导入失败，使用此文件内的备份函数（将yolo8.py的核心函数复制到这里）
    # ... (这里可以粘贴 yolo8.py 的核心处理函数作为备用) ...
    # 为了简洁，此处省略，假设能正常导入


class YoloDepthFusionNode(Node):
    def __init__(self, model_path, target_class='cat',serial_port='/dev/ttyS9', baudrate=115200):
        super().__init__('yolo_depth_fusion_node')
        self.get_logger().info("YOLO 深度融合节点初始化...")

        # --- 初始化模型和图像转换工具 ---
        self.model = Model(model_path)
        self.bridge = CvBridge()
        self.target_class = target_class.lower() # 将目标类别转为小写以方便比较

        # --- 图像和深度图的同步订阅 ---
        self.rgb_sub = message_filters.Subscriber(self, Image, '/ascamera/camera_publisher/rgb0/image')
        self.depth_sub = message_filters.Subscriber(self, Image, '/ascamera/camera_publisher/depth0/image_raw')

        # 同步器
        self.time_synchronizer = message_filters.ApproximateTimeSynchronizer(
            [self.rgb_sub, self.depth_sub],
            queue_size=10,
            slop=0.2 # 允许更大的时间戳差异，以防图像流稍有不同步
        )
        self.time_synchronizer.registerCallback(self.synced_callback)

        self.get_logger().info(f"节点已启动，正在追踪目标: '{self.target_class}'")
        self.get_logger().info("等待同步的RGB和深度图像...")

        # 初始化串口通信
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.ser = None
        self.init_serial()

        self.center_x = 0
        self.center_y = 0
        self.depth_value = 0


    def init_serial(self):
        """初始化串口连接"""
        try:
            # 尝试打开串口
            self.ser = serial.Serial(
                port=self.serial_port,
                baudrate=self.baudrate,
                timeout=0.1  # 读取超时设置
            )
            self.get_logger().info(f"串口已连接: {self.serial_port}, 波特率: {self.baudrate}")
        except serial.SerialException as e:
            self.get_logger().error(f"无法连接到串口 {self.serial_port}: {e}")
            self.ser = None

    def send_data_over_serial(self):
        """通过串口发送数据"""
        if self.ser is None or not self.ser.is_open:
            # 如果串口未打开，尝试重新连接
            self.init_serial()
            if self.ser is None or not self.ser.is_open:
                return False
                
        # 检查是否有有效的数据可发送
        if self.center_x >= 0 and self.center_y >= 0 and self.depth_value >= 0:
            try:
                # 格式化数据为JSON字符串
                data_string = f"X{self.center_x:04d}Y{self.center_y:04d}Z{self.depth_value:06d}\n"
                
                # 发送数据
                self.ser.write(data_string.encode('utf-8'))
                self.get_logger().debug(f"已发送数据: {data_string.strip()}")
                return True
            except Exception as e:
                self.get_logger().error(f"发送数据时出错: {e}")
                self.ser.close()
                self.ser = None
                return False
        return False


    def synced_callback(self, rgb_msg, depth_msg):
        """ 当收到同步的RGB和深度图像时，此函数被调用。 """
        try:
            # 输出图像分辨率
            #self.get_logger().info(f"RGB图像分辨率: {rgb_msg.width}x{rgb_msg.height}")
            #self.get_logger().info(f"深度图像分辨率: {depth_msg.width}x{depth_msg.height}")
            # 1. 图像转换
            cv_image_rgb = self.bridge.imgmsg_to_cv2(rgb_msg, 'bgr8')
            cv_image_depth = self.bridge.imgmsg_to_cv2(depth_msg, '16UC1')

            # 2. 运行YOLO推理
            yolo_result = self.model.inference(cv_image_rgb)
            boxes, classes, scores = yolov8_post_process(yolo_result) if yolo_result else (None, None, None)

            # 3. 查找目标并获取深度
            if boxes is not None:
                # 绘制所有检测框用于显示
                display_image = draw(cv_image_rgb.copy(), boxes, scores, classes)

                for box, score, cl in zip(boxes, scores, classes):
                    class_name = CLASSES[cl].lower()
                    
                    # 检查是否是我们感兴趣的目标
                    if class_name == self.target_class:
                        # 计算边界框的中心点
                        left, top, right, bottom = [int(b) for b in box]
                        #print(top, left, right, bottom)
                        self.center_x = (left + right) // 2
                        self.center_y = (top + bottom) // 2

                        # 确保中心点在图像范围内
                        if 0 <= self.center_y < cv_image_depth.shape[0] and 0 <= self.center_x < cv_image_depth.shape[1]:
                            # 获取中心点的深度值
                            self.depth_value = cv_image_depth[self.center_y, self.center_x]
                            log_message = (f"检测到目标: '{class_name.capitalize()}'! "
                                           f"中心点坐标: ({self.center_x}, {self.center_y}), "
                                           f"深度值: {self.depth_value} 毫米 (mm)")
                            
                            if self.depth_value == 0:
                                log_message += " (注意: 0 通常表示无效值)"
                            
                            self.get_logger().info(log_message)

                            self.send_data_over_serial()

                            # 在图像上标记中心点和深度值
                            cv2.circle(display_image, (self.center_x, self.center_y), 5, (0, 0, 255), -1)
                            cv2.putText(display_image, f"{self.depth_value}mm", (self.center_x + 10, self.center_y + 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        else:
                            self.get_logger().warn(f"目标 '{class_name}' 的中心点 ({self.center_x}, {self.center_y}) 超出图像范围。")

            else:
                # 如果没有检测到任何物体，也显示原始图像
                display_image = cv_image_rgb

            # 4. 显示结果图像 (可选，用于调试)
            cv2.imshow("YOLO Depth Fusion Result", display_image)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"处理同步图像时出错: {e}", exc_info=True)


def main(args=None):
    rclpy.init(args=args)
    
    # --- 参数配置 ---
    # 请确保路径正确
    yolo_model_path = '/home/elf/ros_ws/src/camera_image_display/camera_image_display/yolov8.rknn'
    # 你想追踪的目标类别，请从 CLASSES 列表中选择一个
    target_to_track = 'cat' 

    node = YoloDepthFusionNode(model_path=yolo_model_path, target_class=target_to_track)
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("节点被中断，正在关闭...")
    finally:
        node.get_logger().info("释放模型资源...")
        node.model.release()
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
