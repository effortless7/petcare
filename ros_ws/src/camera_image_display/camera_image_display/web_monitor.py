from flask import Flask, render_template, Response, send_file
import os
import time

app = Flask(__name__)

# 视频流读取函数（读取最新保存的图像）
def generate_video_stream():
    while True:
        if os.path.exists('/tmp/camera_image_for_llm.jpg'):
            with open('/tmp/camera_image_for_llm.jpg', 'rb') as f:
                frame = f.read()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    try:
        with open('/tmp/llm_result.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "大模型结果尚未生成..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
