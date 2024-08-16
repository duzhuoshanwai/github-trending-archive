import os
import subprocess
import requests

# 获取仓库信息和当前提交的 SHA 值
REPO = os.getenv('GITHUB_REPOSITORY')
SHA = os.getenv('GITHUB_SHA')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # 从环境变量获取 Webhook URL

def get_new_files():
    # 使用 Git 命令获取新增的文件列表
    result = subprocess.run(['git', 'diff', '--name-status', 'HEAD~1', 'HEAD'], stdout=subprocess.PIPE)
    files = result.stdout.decode('utf-8').splitlines()
    new_files = [line.split('\t')[1] for line in files if line.startswith('A')]
    return new_files

def send_webhook(file, raw_url):
    # 发送 POST 请求到 Webhook
    payload = {
        'file': file,
        'raw_url': raw_url
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print(f"成功发送通知: {file}")
    else:
        print(f"发送通知失败: {file}，状态码: {response.status_code}")

def main():
    new_files = get_new_files()
    if not new_files:
        print("没有新文件被添加。")
        return

    for file in new_files:
        raw_url = f"https://raw.githubusercontent.com/{REPO}/{SHA}/{file}"
        send_webhook(file, raw_url)

if __name__ == '__main__':
    main()
