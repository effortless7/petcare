# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import message_filters # 用于同步图像话题

class RgbdDepthReaderNode(Node):
    def __init__(self):
        super().__init__('rgbd_depth_reader_node')
        self.bridge = CvBridge()

        # --- 图像和深度图的同步订阅 ---
        # 订阅RGB图像话题
        self.rgb_sub = message_filters.Subscriber(
            self,
            Image,
            '/ascamera/camera_publisher/rgb0/image'
        )
        # 订阅深度图像话题 (raw)
        self.depth_sub = message_filters.Subscriber(
            self,
            Image,
            '/ascamera/camera_publisher/depth0/image_raw'
        )

        # 使用 ApproximateTimeSynchronizer 来同步收到的消息
        # slop参数允许时间戳有微小的差异
        self.time_synchronizer = message_filters.ApproximateTimeSynchronizer(
            [self.rgb_sub, self.depth_sub],
            queue_size=10,
            slop=0.1  # 100ms
        )
        # 注册同步后的回调函数
        self.time_synchronizer.registerCallback(self.synced_callback)

        # --- OpenCV 窗口和鼠标回调 ---
        self.window_name = "RGB Image - Click to get depth"
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

        # 用于存储最新同步到的图像
        self.latest_rgb_image = None
        self.latest_depth_image = None
        
        # 创建一个定时器来刷新显示，避免阻塞spin
        self.timer = self.create_timer(1.0/30.0, self.display_timer_callback)

        self.get_logger().info("深度读取节点已启动。请在弹出的窗口中点击以获取深度值。")

    def synced_callback(self, rgb_msg, depth_msg):
        """
        当收到同步的RGB和深度图像时，此函数被调用。
        """
        try:
            # 转换ROS图像消息为OpenCV图像
            self.latest_rgb_image = self.bridge.imgmsg_to_cv2(rgb_msg, 'bgr8')
            # 深度图通常是16位单通道 (16UC1)，单位是毫米
            self.latest_depth_image = self.bridge.imgmsg_to_cv2(depth_msg, '16UC1')
        except Exception as e:
            self.get_logger().error(f"图像转换失败: {e}")

    def display_timer_callback(self):
        """
        定时刷新OpenCV窗口显示。
        """
        if self.latest_rgb_image is not None:
            cv2.imshow(self.window_name, self.latest_rgb_image)
            cv2.waitKey(1)

    def mouse_callback(self, event, x, y, flags, param):
        """
        处理鼠标点击事件。
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.latest_depth_image is not None:
                # 检查坐标是否在图像范围内
                if 0 <= y < self.latest_depth_image.shape[0] and 0 <= x < self.latest_depth_image.shape[1]:
                    # 获取深度值 (y, x)
                    depth_value = self.latest_depth_image[y, x]
                    
                    log_message = f"坐标 ({x}, {y}) 的深度值为: {depth_value} 毫米 (mm)"
                    if depth_value == 0:
                        log_message += " (注意: 0 通常表示无效值或超出范围)"
                    
                    self.get_logger().info(log_message)
                else:
                    self.get_logger().warn(f"点击坐标 ({x}, {y}) 超出图像范围。")
            else:
                self.get_logger().warn("尚未收到深度图像，无法查询。")

def main(args=None):
    rclpy.init(args=args)
    node = RgbdDepthReaderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('节点被中断，正在关闭...')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main() 