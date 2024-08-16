import os
import subprocess
import requests
from datetime import datetime

# 获取仓库信息和当前提交的 SHA 值
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # 从环境变量获取 Webhook URL

def send_webhook():
    # 获取当前日期并格式化为 YYYY-MM 和 YYYY-MM-DD
    now = datetime.now()
    yyyy_mm = now.strftime('%Y-%m')
    yyyy_mm_dd = now.strftime('%Y-%m-%d')

    # 构建 GitHub 文件的 URL
    url = f'https://github.com/duzhuoshanwai/github-trending-archive/tree/master/data/{yyyy_mm}/{yyyy_mm_dd}.md'


    # 发送 POST 请求到 Webhook
    headers = {"Content-Type": "text/plain"}
    response = requests.post(WEBHOOK_URL, headers=headers,data=url)

    if response.status_code == 200:
        print(f"成功发送通知: {url}")
    else:
        print(f"发送通知失败，状态码: {response.status_code}")

def main():
    send_webhook()

if __name__ == '__main__':
    main()
