import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import subprocess
import os

class CameraImageDisplay(Node):
    def __init__(self, model_path, demo_path, temp_image_path):
        super().__init__('camera_image_display')
        self.bridge = CvBridge()
        self.model_path = model_path
        self.demo_path = demo_path
        self.temp_image_path = temp_image_path
        self.image_sub = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.image_callback,
            10)
        self.image_sub  # 防止未使用的变量警告

    def image_callback(self, msg):
        try:
            # 将 ROS 图像消息转换为 OpenCV 图像
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

            # 保存图像为临时文件
            try:
                self.get_logger().info("尝试保存图像...")
                cv2.imwrite(self.temp_image_path, cv_image)
                self.get_logger().info(f"图像已成功保存到 {self.temp_image_path}")
            except Exception as e:
                self.get_logger().error(f"保存图像时出错: {e}")

            # 调用 YOLOv8 目标检测 demo
            result = subprocess.run([self.demo_path, self.model_path, self.temp_image_path], capture_output=True, text=True)

            # 处理推理结果
            output = result.stdout
            print("推理结果：")
            print(output)

            # 显示标注后的图像（如果有）
            annotated_image_path = "out.png"
            if os.path.exists(annotated_image_path):
                annotated_image = cv2.imread(annotated_image_path)
                cv2.imshow('Annotated Camera Image', annotated_image)
            else:
                self.get_logger().info("未找到标注后的图像文件")

            # 显示原始图像
            cv2.imshow('Camera Image', cv_image)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")

def main(args=None):
    rclpy.init(args=args)
    # 为变量赋合适的值
    model_path = "/home/elf/Desktop/my_rknn_yolov8_demo/model/yolov8.rknn"
    demo_path = "/home/elf/Desktop/my_rknn_yolov8_demo/rknn_yolov8_demo"
    temp_image_path = "/home/elf/Desktop/my_rknn_yolov8_demo/camera_image.jpg"
    image_display = CameraImageDisplay(model_path, demo_path, temp_image_path)
    rclpy.spin(image_display)
    image_display.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    
