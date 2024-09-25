import os
import requests
import random

# トピックのディレクトリ
TOPICS_DIR = 'topics'

# トピックディレクトリからランダムにファイルを選び、その内容を読み込む関数
def load_topics(dir_path):
    topic_files = os.listdir(dir_path)
    random_selected_file = random.choice(topic_files)
    file_path = os.path.join(dir_path, random_selected_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# トピックを読み込み、ランダムに選ぶ
topics = load_topics(TOPICS_FILE)
message = random.choice(topics)

# Slack Webhook URL
slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')

# Slackにメッセージを送信
def send_message_to_slack(message: str):
    payload = {
        "text": f"雑談しましょう！ 今日の話題: {message}"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(slack_webhook_url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request to Slack returned error {response.status_code}, the response is:\n{response.text}")

send_message_to_slack(message)