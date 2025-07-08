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

GOAWAY_WAV_PATH = '/home/elf/ros_ws/src/camera_image_display/camera_image_display/gogo.wav'

class GoAwayPlayer:
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
            self._thread = None  # 清理线程对象


class LlmAntoNode(Node):
    def __init__(self):
        super().__init__('llm_auto_node')
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
        self._lock = threading.Lock()
        self.is_playing_abnormal = False  # 记录是否当前在播放

    def image_callback(self, msg):
        with self._lock:
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
                                'text': """
                                You are a pet behavior analysis assistant. Carefully observe the provided image and determine if there is an animal present. If you detect an animal, identify its behavior and judge whether it is normal. If you do not see any animal at all, then output "No animal detected".

                                Your output must strictly be in JSON format like this:
                                {
                                "content": "<A concise summary of the observed pet action or situation in the image. If no animal is detected, write 'No animal detected'.>",
                                "conclusion": "<Choose one of 'Normal', 'Abnormal', or 'No animal detected' as the only allowed conclusion>"
                                }

                                Important requirements:
                                - You MUST first detect whether there is an animal in the image. If any animal is present, even if the behavior seems unclear, you must NOT output "No animal detected"; you must describe what you see and provide a conclusion.
                                - Only output a single JSON object. Do not add any extra text, comments, or explanations.
                                - The conclusion field must strictly be one of "Normal", "Abnormal", or "No animal detected" — do not use any other words or variants.
                                - The content field should be a concise, accurate description of the observed situation.
                                - You must identify what the animal is actually doing, not just its location or position. Carefully distinguish whether the animal is interacting with inappropriate items (e.g., rummaging through trash cans, tearing furniture, urinating in inappropriate places) and judge the behavior accordingly. Do not assume objects; verify carefully whether it is a trash can, litter box, or something else before making a judgment.

                                Examples of abnormal behaviors (including but not limited to, please generalize to similar destructive or aggressive behaviors):
                                - Knocking over items
                                - Rummaging /looking through trash cans
                                - Sitting on a sofa (if accompanied by chewing or destruction)
                                - Destroying furniture (chewing, tearing)
                                - Barking
                                - Urinating in inappropriate places
                                - Scratching furniture or other items
                                - Performing other clearly inappropriate, destructive, or aggressive actions

                                Examples:
                                (Example: an image showing a dog quietly sleeping on a sofa)
                                Output:
                                {
                                "content": "Dog sleeping on the sofa",
                                "conclusion": "Normal"
                                }

                                (Example: an image showing a cat tearing up the sofa)
                                Output:
                                {
                                "content": "Cat tearing the sofa",
                                "conclusion": "Abnormal"
                                }

                                (Example: an image showing a cat looking through trash cans)
                                Output:
                                {
                                "content": "cat playing with a trash can",
                                "conclusion": "Abnormal"
                                }

                                (Example: an image showing an empty room with no animals)
                                Output:
                                {
                                "content": "No animal detected",
                                "conclusion": "No animal detected"
                                }

                                Now, please generate the output JSON based on the uploaded image.
                            """
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
                abnormal_keywords = ['Abnormal']
                is_abnormal = any(keyword in llm_output for keyword in abnormal_keywords)
                print('1')

                if is_abnormal:
                    if not self.is_playing_abnormal:
                        self.get_logger().info("检测到异常行为，循环播放goaway.wav三次！")
                        self.goaway_player.start(n=3)
                        self.is_playing_abnormal = True
                    else:
                        self.get_logger().info("异常行为仍在持续，但已播放三次。")
                else:
                    if self.is_playing_abnormal:
                        self.get_logger().info("异常行为已停止，停止播放goaway.wav。")
                        self.goaway_player.stop()
                        self.is_playing_abnormal = False
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
