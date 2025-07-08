# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import requests
import base64
import json
import threading
import time
import subprocess

GOAWAY_WAV_PATH = os.path.join(os.path.dirname(__file__), 'goaway.wav')

class GoAwayPlayer:
    """
    循环播放goaway.wav，直到stop被调用。
    """
    def __init__(self, wav_path):
        self.wav_path = wav_path
        self._stop_event = threading.Event()
        self._thread = None

    def _play_loop(self):
        while not self._stop_event.is_set():
            try:
                subprocess.run(['aplay', self.wav_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                print(f"播放goaway.wav时出错: {e}")
            # 可选：每次播放后短暂休眠，避免过快重复
            time.sleep(0.1)

    def start(self):
        if self._thread and self._thread.is_alive():
            return  # 已在播放
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._play_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=2)

class LlmAntoNode(Node):
    def __init__(self):
        super().__init__('llm_anto_node')
        self.bridge = CvBridge()
        self.temp_image_path = "/tmp/camera_image_for_llm.jpg"
        self.llm_server_url = 'http://localhost:8090/v1/chat/completions'
        self.llm_model_name = 'RK3588-Qwen2-VL-2B'
        self.image_sub = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.image_callback,
            10
        )
        self.get_logger().info("llm_anto_node已启动，等待图像输入...")
        self.goaway_player = GoAwayPlayer(GOAWAY_WAV_PATH)
        self._lock = threading.Lock()  # 控制并发

    def image_callback(self, msg):
        with self._lock:
            # 每次新分析前，先停止goaway.wav
            self.goaway_player.stop()
            try:
                cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
                cv2.imwrite(self.temp_image_path, cv_image)
                self.get_logger().info(f"图像已保存到 {self.temp_image_path}，准备推理...")
            except Exception as e:
                self.get_logger().error(f"保存图像失败: {e}")
                return
            try:
                with open(self.temp_image_path, 'rb') as img_file:
                    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
            except Exception as e:
                self.get_logger().error(f"读取图像文件失败: {e}")
                return
            request_data = {
                'model': self.llm_model_name,
                'messages': [
                    {
                        'role': 'user',
                        'content': [
                            {
                                'type': 'image_url',
                                'image_url': {
                                    'url': f'data:image/jpeg;base64,{img_base64}'
                                }
                            },
                            {
                                'type': 'text',
                                'text': '描述这张图片的内容，如果有宠物，请重点观察宠物的动作是否异常，异常动作包括：打翻东西、垃圾桶、坐在沙发上、拆家、吠叫、在不应该的地方尿尿等等。如果有，请描述异常动作，并在输出的最后加yes'
                            }
                        ]
                    }
                ],
                'stream': False
            }
            self.get_logger().info('发送请求中...')
            try:
                response = requests.post(
                    self.llm_server_url,
                    json=request_data,
                    stream=True,
                    timeout=60
                )
                data = response.json()
                llm_output = data['choices'][0]['message']['content']
                self.get_logger().info(f"大模型输出: {llm_output}")
                abnormal_keywords = ['沙发', '垃圾桶', '咬', '破坏', '打翻', '尿', '吠叫', '抓', 'yes']
                is_abnormal = any(keyword in llm_output for keyword in abnormal_keywords)
                if is_abnormal:
                    self.get_logger().info("检测到异常行为，开始循环播放goaway.wav！")
                    self.goaway_player.start()
                else:
                    self.get_logger().info("未检测到异常行为。")
            except Exception as e:
                self.get_logger().error(f"大模型推理或解析响应时出错: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = LlmAntoNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('节点被中断，正在关闭...')
    finally:
        node.goaway_player.stop()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 