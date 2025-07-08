from datetime import datetime
import requests

APP_ID = "cli_a8ef9e721d39900b"
APP_SECRET = "ABRt59wsuB5dot3KWPB80dRtXd3LJfqb"
APP_TOKEN = "XEvXbP9r2a8Uvgsoovnc2VsfnsN"   # Base ID
TABLE_ID = "tblWTRHpbviYVND9"

# 字段 ID 映射
FIELD_IDS = {
    "timestamp": "fld7VbMLpp",  # 主字段，文本
    "abnormal": "fldOWDNEHZ",   # 文本
    "content": "fldckz0fmu",    # 文本
}

def get_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    resp = requests.post(url, json=payload)
    data = resp.json()
    if data.get("code") == 0:
        return data["tenant_access_token"]
    else:
        raise Exception(f"获取token失败: {data}")

def write_log(token, content, is_abnormal):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    # 主字段内容必须唯一，这里用时间戳做唯一标识
    unique_id = f"log_{int(datetime.now().timestamp())}"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "records": [
            {
                "fields": {
                    FIELD_IDS["timestamp"]: unique_id,
                    FIELD_IDS["abnormal"]: "是" if is_abnormal else "否",
                    FIELD_IDS["content"]: content,
                }
            }
        ]
    }

    print("📤 请求数据：", data)

    response = requests.post(url, headers=headers, json=data)
    print("状态码:", response.status_code)
    print("返回内容:", response.text)


if __name__ == "__main__":
    token = get_access_token()
    write_log(token, "🐾 测试日志：宠物跳上沙发", True)
