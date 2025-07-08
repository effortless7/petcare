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
from camera_image_display.feishu_logger import write_log_to_feishu

speaker = Speaker.get_instance()

class RosLlmInferenceNode(Node):
    def __init__(self):
        super().__init__('ros_llm_inference_node')
        self.bridge = CvBridge()
        self.temp_image_path = "/tmp/camera_image_for_llm.jpg"

        # 大模型服务器与模型配置
        self.llm_server_url = 'http://localhost:8090/v1/chat/completions'
        self.llm_model_name = 'RK3588-Qwen2-VL-2B'
        
        # IMGBB API配置
        self.imgbb_api_key = "98ef33da522c2d20ec2b64f123899994"
        self.imgbb_api_url = "https://api.imgbb.com/1/upload"

        self.image_sub = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.image_callback,
            10
        )

        self.image_sub
        self.get_logger().info("ROS LLM 推理节点已启动，等待图像输入...")

    def upload_to_imgbb(self, image_path):
        """上传图片到IMGBB并返回URL"""
        try:
            with open(image_path, "rb") as file:
                payload = {
                    "key": self.imgbb_api_key,
                    "image": base64.b64encode(file.read()),
                }
                
                response = requests.post(self.imgbb_api_url, data=payload)
                data = response.json()
                
                if response.status_code == 200 and data.get("success"):
                    return data["data"]["url"]
                else:
                    self.get_logger().error(f"IMGBB上传失败: {data.get('error', '未知错误')}")
                    return None
        except Exception as e:
            self.get_logger().error(f"IMGBB上传异常: {e}")
            return None

    def send_message_to_server(self, content):
        url = "http://tencent.wishzone.top:8385/message?token=ASESO9zekeDW-Pq"
        image_path = self.temp_image_path
        
        try:
            # 上传图片到 imgbb 获取公开 URL
            image_url = self.upload_to_imgbb(image_path)
            
            if not image_url:
                self.get_logger().error("无法获取图片URL，使用本地路径作为兜底")
                image_url = "https://i.ibb.co/5hwzP76z/dbbbec09c851.jpg"  # 使用一个默认图像 URL
            
            # 构建消息数据，包含点击跳转与大图展示
            message_data = {
                "title": "异常行为",
                "message": content,
                "priority": 8,
                "extras": {
                    "client::notification": {
                        "click": {
                            "url": image_url
                        },
                        "bigImageUrl": image_url
                    }
                }
            }

            # 发送 JSON 消息
            response = requests.post(
                url,
                json=message_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )

            if response.status_code == 200:
                self.get_logger().info(f"✅ 消息（附带图片）已成功发送，响应内容: {response.text}")
            else:
                self.get_logger().error(f"❌ 消息发送失败，状态码: {response.status_code}, 响应内容: {response.text}")
        
        except Exception as e:
            self.get_logger().error(f"❌ 发送消息时发生异常: {e}")


    def image_callback(self, msg):
        try:
            # ROS 图像转 OpenCV 图像
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

            try:
                cv2.imwrite(self.temp_image_path, cv_image)
                self.get_logger().info(f"图像已成功保存到 {self.temp_image_path}，准备进行大模型推理...")
            except Exception as e:
                self.get_logger().error(f"保存图像时出错: {e}")
                return

            with open(self.temp_image_path, 'rb') as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

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
                                'text': '描述这张图片的内容，如果有宠物，请重点观察宠物的动作'
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

                print("\n大模型描述完成。")
                self.get_logger().info(f"大模型完整输出: {llm_output}")
                abnormal_keywords = ['沙发', '垃圾桶', '咬', '破坏', '打翻', '尿', '吠叫', '抓' , 'yes']
                is_abnormal = any(keyword in llm_output for keyword in abnormal_keywords)

                safe_output = llm_output.replace('\n', ' ')
                if is_abnormal:
                    self.get_logger().info(f"🔔 正在发送到服务器: {safe_output}")
                    self.send_message_to_server(safe_output)
                    write_log_to_feishu(safe_output, is_abnormal)

            except requests.exceptions.Timeout:
                self.get_logger().error("连接大模型服务器超时。请检查网络或服务器状态。")
            except requests.exceptions.ConnectionError as ce:
                self.get_logger().error(f"连接大模型服务器失败: {ce}。请确保服务器已运行且地址正确。")
            except Exception as ex:
                self.get_logger().error(f"大模型请求处理时发生未知错误: {ex}")

        except Exception as e:
            self.get_logger().error(f"处理图像或调用大模型时发生错误: {e}")

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
