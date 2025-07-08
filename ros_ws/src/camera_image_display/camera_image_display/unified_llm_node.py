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
import websocket
from camera_image_display.tts_wrapper import Speaker
import time
import urllib3

# 关闭 InsecureRequestWarning 警告（因为 WMHUA 证书跳过验证）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 语音播报实例
speaker = Speaker.get_instance()

# WebSocket配置
WS_URL = "ws://43.138.135.187:8385/stream"
WS_TOKEN = "CgC0IeIxTqamAf_"
WS_HEADER = [f"X-Gotify-Key: {WS_TOKEN}"]

# HTTP消息推送配置
HTTP_PUSH_URL = "http://tencent.wishzone.top:8385/message?token=ASESO9zekeDW-Pq"

# IMGBB配置
IMGBB_API_KEY = "98ef33da522c2d20ec2b64f123899994"
IMGBB_API_URL = "https://api.imgbb.com/1/upload"

# WMHUA备用图床配置
WMHUA_UPLOAD_URL = "https://www.wmhua.cn/api/v1/upload"
WMHUA_AUTH_TOKEN = "F7RxSxqAjGP631gtee1BHEaNKtr4MGfmqKdsUnNb"

IMGURL_UPLOAD_URL = "https://imgurl.org/api/v2/upload"
IMGURL_API_TOKEN = "39f16defc4ca4e21b58b54daec5b0104"
# 大模型推理配置
LLM_SERVER_URL = 'http://localhost:8090/v1/chat/completions'
LLM_MODEL_NAME = 'RK3588-Qwen2-VL-2B'

# 默认图片路径
TEMP_IMAGE_PATH = "/tmp/camera_image_for_llm.jpg"

# 模式说明（模式1不播报）
MODE_DESC = {
    1: "异常时仅推送消息",
    2: "异常时推送+播报托管消息（title=\"托管\"）",
    3: "异常时仅播报托管消息",
    4: "全部推送，异常时播报托管消息"
}

class UnifiedLLMNode(Node):
    def __init__(self):
        super().__init__('unified_llm_node')
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(
            Image,
            '/ascamera/camera_publisher/rgb0/image',
            self.image_callback,
            10
        )
        self.get_logger().info("统一大模型节点已启动，等待图像输入...")

        # 状态变量（带锁保护）
        self.mode = 4
        self.custom_title = "模式"
        self.custom_message = ""
        self.trusted_message = ""
        self.next_mode = None  # 下一次生效的模式
        self.lock = threading.RLock()  # 可重入锁

        # 启动WebSocket线程
        self.ws_running = True
        self.ws_thread = threading.Thread(target=self.run_websocket, daemon=True)
        self.ws_thread.start()

        # ROS Executor 用于安全跨线程播报
        self.executor = self.get_node_executor()

    def get_node_executor(self):
        # 尽量获取当前节点的 executor（rclpy 2.0 及以上支持）
        # 如果不存在，可以改为同步调用
        try:
            return rclpy.get_default_context().get_executor()
        except Exception:
            return None

    def run_websocket(self):
        """WebSocket线程主函数，包含重连逻辑"""
        while self.ws_running:
            try:
                self._run_websocket_once()
            except Exception as e:
                self.get_logger().error(f"WebSocket线程异常: {e}")
                time.sleep(5)

    def _run_websocket_once(self):
        """单次WebSocket连接逻辑"""
        def on_message(ws, message):
            try:
                data = json.loads(message)
                title = data.get("title", "")
                msg = data.get("message", "")

                with self.lock:
                    if title == "播报" and msg:
                        self.get_logger().info(f"[WS] 收到一次性播报消息：{msg}")
                        self._safe_speak(msg)

                    elif title == "托管" and msg:
                        self.trusted_message = msg
                        self.get_logger().info(f"[WS] 设置托管播报内容：{msg}")

                    elif title == "模式" and msg:
                        try:
                            mode = int(msg)
                            if mode in MODE_DESC:
                                self.mode = mode
                                self.get_logger().info(f"[WS] 模式切换为 {mode}: {MODE_DESC[mode]}")
                        except ValueError:
                            self.get_logger().warn(f"[WS] 模式设置失败，无法转换为整数: {msg}")

            except Exception as e:
                self.get_logger().error(f"[WS] 处理消息出错: {e}")

        def on_error(ws, error):
            self.get_logger().error(f"[WS] 错误: {error}")

        def on_close(ws, code, msg):
            self.get_logger().info(f"[WS] 连接关闭，5秒后重连...")

        def on_open(ws):
            self.get_logger().info("[WS] 连接成功")

        ws = websocket.WebSocketApp(
            WS_URL,
            header=WS_HEADER,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        ws.on_open = on_open
        ws.run_forever()

    def _safe_speak(self, content):
        """跨线程安全的语音播报"""
        try:
            if self.executor:
                self.executor.create_task(lambda: speaker.speak(content))
            else:
                # 没有 executor，直接同步播报（可能阻塞）
                speaker.speak(content)
            self.get_logger().info(f"🔊 播报: {content}")
        except Exception as e:
            self.get_logger().error(f"语音播报异常: {e}")

    def upload_to_imgurl_by_file(self, image_path):
        try:
            with open(image_path, "rb") as f:
                files = {
                    'file': ('image.jpg', f, 'image/jpeg')
                }
                headers = {
                    "Authorization": "Token 39f16defc4ca4e21b58b54daec5b0104"
                }
                response = requests.post(
                    IMGURL_UPLOAD_URL,
                    headers=headers,
                    files=files,
                    timeout=10
                )
            data = response.json()
            if data.get("code") == 200 and data.get("data", {}).get("url"):
                return data["data"]["url"]
            else:
                print(f"IMGURL 上传失败: {data.get('msg', '未知错误')}")
                return None
        except Exception as e:
            print(f"上传异常: {e}")
            return None

    def upload_image_with_backup(self, image_path):
        """优先用 IMGBB 上传，失败自动切换 WMHUA 图床"""
        # 先尝试 IMGBB
        try:
            with open(image_path, "rb") as file:
                payload = {
                    "key": IMGBB_API_KEY,
                    "image": base64.b64encode(file.read()),
                }
            imgbb_resp = requests.post(IMGBB_API_URL, data=payload, timeout=10)
            imgbb_data = imgbb_resp.json()
            if imgbb_resp.status_code == 200 and imgbb_data.get("success"):
                return imgbb_data["data"]["url"]
            else:
                self.get_logger().warning(f"IMGBB 上传失败: {imgbb_data.get('error', '未知错误')}")
        except Exception as e:
            self.get_logger().warning(f"IMGBB 上传异常: {str(e)}")
            return url if url else "https://i.ibb.co/5hwzP76z/dbbbec09c851.jpg"

        # IMGBB 失败，尝试 IMGURL 备用图床
        #print("使用 IMGURL 作为备份上传...")
        #url = self.upload_to_imgurl_by_file(image_path)
        

    def send_message_to_server(self, content, image_path=TEMP_IMAGE_PATH):
        """发送带图片的异常消息至服务器，确保图片与描述对应"""
        try:
            image_url = self.upload_image_with_backup(image_path)
            message_data = {
                "title": "行为监测",
                "message": content,
                "priority": 8,
                "extras": {
                    "client::notification": {
                        "click": {"url": image_url},
                        "bigImageUrl": image_url
                    }
                }
            }
            response = requests.post(
                HTTP_PUSH_URL,
                json=message_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            if response.status_code == 200:
                self.get_logger().info(f"✅ 消息已发送: {response.text[:50]}...")
            else:
                self.get_logger().error(f"❌ 消息发送失败: HTTP {response.status_code}")
        except Exception as e:
            self.get_logger().error(f"❌ 发送消息异常: {str(e)}")

    def image_callback(self, msg):
        """图像回调函数，包含完整大模型处理流程"""
        # 模式切换
        with self.lock:
            if self.next_mode is not None:
                self.mode = self.next_mode
                self.get_logger().info(f"当前模式更新为 {self.mode}: {MODE_DESC[self.mode]}")
                self.next_mode = None

        # 1. 图像转换与保存
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            cv2.imwrite(TEMP_IMAGE_PATH, cv_image)
            self.get_logger().info("图像已保存，准备大模型推理")
        except Exception as e:
            self.get_logger().error(f"图像处理失败: {str(e)}")
            return

        # 2. 读取图片并编码 base64
        try:
            with open(TEMP_IMAGE_PATH, 'rb') as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
        except Exception as e:
            self.get_logger().error(f"图像读取失败: {str(e)}")
            return

        # 3. 构造大模型请求
        request_data = {
            'model': LLM_MODEL_NAME,
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
                            "content": "Cat looking through trash cans",
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

        # 4. 调用大模型API
        try:
            response = requests.post(
                LLM_SERVER_URL,
                json=request_data,
                headers={"Content-Type": "application/json"},
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            llm_output = data['choices'][0]['message']['content']
            self.get_logger().info(f"大模型响应: {llm_output[:100]}...")
        except requests.exceptions.RequestException as e:
            self.get_logger().error(f"大模型请求失败: {str(e)}")
            return
        except (KeyError, IndexError) as e:
            self.get_logger().error(f"大模型响应解析失败: {str(e)}，响应内容: {response.text[:200]}...")
            return
        except Exception as e:
            self.get_logger().error(f"大模型处理异常: {str(e)}")
            return

        # 5. 解析大模型输出
        try:
            llm_output_cleaned = llm_output.strip()
            if llm_output_cleaned.startswith("```json"):
                llm_output_cleaned = llm_output_cleaned[7:].strip()
            if llm_output_cleaned.endswith("```"):
                llm_output_cleaned = llm_output_cleaned[:-3].strip()

            result = json.loads(llm_output_cleaned)
            conclusion = result.get("conclusion", "")
            content = result.get("content", "")
            self.get_logger().info(f"解析结果 - 结论: {conclusion}, 内容: {content}")
        except json.JSONDecodeError as e:
            self.get_logger().error(f"JSON解析失败: {str(e)}，原始输出: {llm_output[:100]}...")
            return
        except Exception as e:
            self.get_logger().error(f"结果解析异常: {str(e)}")
            return

        # 6. 根据模式执行逻辑
        is_abnormal = (conclusion == "Abnormal")
        print(f"is_abnormal: {is_abnormal}")
        with self.lock:
            current_mode = self.mode
            current_trusted_msg = self.trusted_message

        if current_mode == 1:
            if is_abnormal:
                self.send_message_to_server(content)
        elif current_mode == 2:
            if is_abnormal:
                self.send_message_to_server(content)
                if current_trusted_msg:
                    self._safe_speak(current_trusted_msg)
        elif current_mode == 3:
            if is_abnormal and current_trusted_msg:
                self._safe_speak(current_trusted_msg)
        elif current_mode == 4:
            self.send_message_to_server(content)
            if is_abnormal and current_trusted_msg:
                self._safe_speak(current_trusted_msg)

    def __del__(self):
        """析构函数，确保线程安全退出"""
        self.ws_running = False
        if hasattr(self, 'ws_thread') and self.ws_thread.is_alive():
            self.ws_thread.join(timeout=2)


def main(args=None):
    rclpy.init(args=args)
    node = UnifiedLLMNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('节点被用户中断')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
