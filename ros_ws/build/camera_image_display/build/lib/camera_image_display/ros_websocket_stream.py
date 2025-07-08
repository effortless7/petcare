# ros_websocket_stream.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import threading
import asyncio
import websockets
import base64
import json

bridge = CvBridge()
latest_frame = None
lock = threading.Lock()

# ROS2 订阅节点
class RosImageListener(Node):
    def __init__(self):
        super().__init__('ros_websocket_stream_node')
        self.subscription = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.listener_callback,
            10)
        self.get_logger().info('WebSocket 图像订阅节点已启动。')

    def listener_callback(self, msg):
        global latest_frame
        try:
            frame = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            frame = cv2.resize(frame, (640, 480))  # 缩小图像尺寸
            with lock:
                latest_frame = frame
        except Exception as e:
            self.get_logger().error(f"图像转换失败: {e}")

# WebSocket 服务端
async def video_stream_handler(websocket, path):
    print(f"客户端连接: {websocket.remote_address}")
    try:
        while True:
            await asyncio.sleep(0.1)
            with lock:
                if latest_frame is not None:
                    _, buffer = cv2.imencode('.jpg', latest_frame)
                    jpg_base64 = base64.b64encode(buffer).decode('utf-8')
                    await websocket.send(json.dumps({"type": "image", "data": jpg_base64}))
    except websockets.exceptions.ConnectionClosed:
        print("客户端断开连接")

# 主程序入口
def main():
    rclpy.init()
    ros_node = RosImageListener()

    # ROS 节点运行在独立线程
    ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=True)
    ros_thread.start()

    # 启动 WebSocket 服务
    start_server = websockets.serve(video_stream_handler, '0.0.0.0', 5680)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket 服务运行在 ws://0.0.0.0:5680")
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()
