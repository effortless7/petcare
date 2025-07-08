import websocket
import json
from camera_image_display.tts_wrapper import Speaker

speaker = Speaker.get_instance()
TARGET_TITLE = "播报"  # 设置需要播报的目标标题

def on_message(ws, message):
    try:
        data = json.loads(message)
        content = data.get("message", "")
        title = data.get("title", "")  # 获取消息标题
        
        print("📩 收到消息:", content)

        # 仅当标题匹配且内容不为空时才进行播报
        if title == TARGET_TITLE and content:
            print(f"🔊 播报标题为 '{title}' 的消息...")
            speaker.speak(content)
        else:
            print(f"ℹ️ 标题不匹配，跳过播报 (标题: '{title}')")
            
    except Exception as e:
        print("❌ 处理消息时出错:", e)

def on_error(ws, error):
    print("❌ 错误:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔌 连接关闭")

def on_open(ws):
    print("✅ 连接成功")

def main():
    token = "CgC0IeIxTqamAf_"  # 替换为你自己的 Token
    url = "ws://43.138.135.187:8385/stream"
    headers = [
        f"X-Gotify-Key: {token}"
    ]

    ws = websocket.WebSocketApp(
        url,
        header=headers,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    main()