# ros_web_video_stream.py
#将相机实时图像推流
#conda deactivate后 python3运行；访问http://10.195.9.1:5050/ros_video_feed
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from flask import Flask, Response
from cv_bridge import CvBridge
import threading
import cv2

app = Flask(__name__)
bridge = CvBridge()

# 全局共享变量
latest_frame = None
lock = threading.Lock()

# Flask 路由：视频流输出
@app.route('/ros_video_feed')
def ros_video_feed():
    def generate():
        while True:
            with lock:
                if latest_frame is not None:
                    _, buffer = cv2.imencode('.jpg', latest_frame)
                    frame_bytes = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')


# ROS 节点线程
class RosImageListener(Node):
    def __init__(self):
        super().__init__('ros_web_video_node')
        self.subscription = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.listener_callback,
            10)
        self.subscription  # 防止警告
        self.get_logger().info("订阅 /ascamera/camera_publisher/rgb0/image 成功。")

    def listener_callback(self, msg):
        global latest_frame
        try:
            frame = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            with lock:
                latest_frame = frame
        except Exception as e:
            self.get_logger().error(f"图像转换失败: {e}")


# 启动函数
def start_flask_ros_server():
    rclpy.init()
    ros_node = RosImageListener()

    # 启动 ROS2 节点线程
    ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=True)
    ros_thread.start()

    # 启动 Flask Web 服务
    app.run(host='0.0.0.0', port=5050, debug=False)


if __name__ == '__main__':
    start_flask_ros_server()
