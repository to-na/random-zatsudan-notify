import os
import requests
import random

# 雑談の話題をリスト化
topics = [
    "最近読んだ本は何ですか？",
    "今週末の予定は？",
    "好きな映画は？",
    "最近ハマっている趣味は？",
    "好きな季節はいつですか？"
]

# ランダムに雑談の話題を選ぶ
message = random.choice(topics)

# Slack Webhook URL
slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')

# Slackにメッセージを送信
def send_message_to_slack(message: str):
    payload = {
        "text": f"今日の雑談の話題: {message}"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(slack_webhook_url, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Request to Slack returned error {response.status_code}, the response is:\n{response.text}")

send_message_to_slack(message)