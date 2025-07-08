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
from camera_image_display.tts_wrapper import Speaker
import threading
from threading import Lock, Event


# === 语音播放控制：始终播放最新内容 ===
speaker = Speaker.get_instance()
latest_text = None
latest_lock = Lock()
play_event = Event()

def speak_worker():
    global latest_text
    while True:
        play_event.wait()
        with latest_lock:
            text = latest_text
            latest_text = None
            play_event.clear()
        if text:
            print(f"🎙️ 正在播报: {text}")
            speaker.speak(text)

# 启动后台语音线程
speak_thread = threading.Thread(target=speak_worker, daemon=True)
speak_thread.start()


# === ROS 推理节点定义 ===
class RosLlmInferenceNode(Node):
    def __init__(self):
        super().__init__('ros_llm_inference_node')
        self.bridge = CvBridge()
        self.temp_image_path = "/tmp/camera_image_for_llm.jpg"
        self.llm_server_url = 'http://localhost:8090/v1/chat/completions'
        self.llm_model_name = 'RK3588-Qwen2-VL-2B'

        self.image_sub = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.image_callback,
            10)
        self.image_sub
        self.get_logger().info("ROS LLM 推理节点已启动，等待图像输入...")

    def image_callback(self, msg):
        try:
            # 转换图像
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

            # 保存为临时图片
            try:
                cv2.imwrite(self.temp_image_path, cv_image)
                self.get_logger().info(f"图像已保存到 {self.temp_image_path}，准备推理...")
            except Exception as e:
                self.get_logger().error(f"保存图像失败: {e}")
                return

            # 编码为 base64
            with open(self.temp_image_path, 'rb') as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

            # 构造请求
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
                                你是一位充满爱心的宠物主人，擅长理解和回应宠物的行为。
                                1.请描述图片内容
                                2.如果图片中有宠物，则根据其动作和状态，用简短、亲切的语言与其互动
                                3.如果图片中没有宠物，则输出"我没看到宠物"
                                互动语言要求：
                                • 仅输出互动内容，不解释或描述图片
                                • 对猫使用可爱亲昵的语气（如"小调皮！"）
                                • 对狗使用热情鼓励的语气（如"好棒！"）
                                • 对其他宠物使用适合其特点的语气                               
                                示例：
                                [如果看到猫在抓玩具] → 输出：小调皮！又在练习捕猎啦~
                                [如果猫在窗边看鸟] → 输出：外面有什么好玩的？想抓小鸟吗？
                                [如果看到狗叼着球等待] → 输出：准备好玩接球游戏了吗？真棒！
                                [如果看到仓鼠在转轮上跑步] → 输出：运动健将！跑这么快不累吗？
                                [如果看到空房间图片] → 输出：我没看到宠物
                                """
                            }
                        ]
                    }
                ],
                'stream': False  # 非流式
            }

            self.get_logger().info('发送请求中...')
            try:
                response = requests.post(self.llm_server_url, json=request_data, timeout=60)
                data = response.json()
                llm_output = ""
                if 'choices' in data and len(data['choices']) > 0:
                    message = data['choices'][0].get('message', {})
                    llm_output = message.get('content', '')
                    print(f"🧠 大模型输出内容：{llm_output}")

                # 写入最新内容
                if llm_output.strip():
                    with latest_lock:
                        global latest_text
                        latest_text = llm_output.strip()
                        play_event.set()

                    with open("/tmp/llm_result.txt", "w") as f:
                        f.write(llm_output.strip())

                self.get_logger().info(f"大模型完整输出: {llm_output}")

            except requests.exceptions.Timeout:
                self.get_logger().error("连接大模型服务器超时。")
            except requests.exceptions.ConnectionError as ce:
                self.get_logger().error(f"连接失败: {ce}")
            except Exception as ex:
                self.get_logger().error(f"未知错误: {ex}")

        except Exception as e:
            self.get_logger().error(f"图像处理或请求时出错: {e}")


# === 启动入口 ===
def main(args=None):
    rclpy.init(args=args)
    node = RosLlmInferenceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('节点被中断，正在关闭...')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
