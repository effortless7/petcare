# feishu_logger.py
import requests
from datetime import datetime

APP_ID = "cli_a8ef9e721d39900b"
APP_SECRET = "ABRt59wsuB5dot3KWPB80dRtXd3LJfqb"
BASE_ID = "XEvXbP9r2a8Uvgsoovnc2VsfnsN"
TABLE_ID = "tblWTRHpbviYVND9"


def get_feishu_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get("tenant_access_token")
    else:
        print("[Feishu] 获取 token 失败:", response.text)
        return None


def write_log_to_feishu(content, is_abnormal):
    token = get_feishu_token()
    if not token:
        return

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{BASE_ID}/tables/{TABLE_ID}/records"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "records": [
            {
                "fields": {
                    "timestamp": now_str,
                    "abnormal": "是" if is_abnormal else "否",
                    "content": content
                }
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("[Feishu] ✅ 写入成功")
    else:
        print("[Feishu] ❌ 写入失败:", response.text)
