import requests
import base64
import json

# 读取图片并转为base64
with open('/home/elf/image/demo.jpg', 'rb') as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# 构造请求
request_data = {
    'model': 'RK3588-Qwen2-VL-2B',
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
                    'text': '描述这张图片的内容'
                }
            ]
        }
    ],
    'stream': True
}

# 发送请求
print('发送请求中...')
response = requests.post('http://localhost:8090/v1/chat/completions', 
                          json=request_data, 
                          stream=True)

# 实时输出结果
print('收到响应:')
for chunk in response.iter_lines():
    if chunk:
        # 过滤data前缀
        text = chunk.decode('utf-8')
        print(text)
        # if text.startswith('data: '):
        #     try:
        #         data = json.loads(text[6:])
        #         if 'choices' in data and len(data['choices']) > 0:
        #             if 'delta' in data['choices'][0] and 'content' in data['choices'][0]['delta']:
        #                 print(data['choices'][0]['delta']['content'], end='', flush=True)
        #     except:
        #         print(text)
