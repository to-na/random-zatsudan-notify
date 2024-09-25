# random-zatsudan-notify

雑談しよう

## これは何

- 雑談トピックをランダムで定時に Slack に通知します。

### 実行例
![スクリーンショット 2024-09-25 20 51 28](https://github.com/user-attachments/assets/eb0c2bdd-7239-460d-a91e-89fa0e3fc844)

## 使い方

1. このリポジトリを fork などして、プライベートリポジトリに置いてください。

2. Webhook の設定

- `https://api.slack.com/messaging/webhooks` で Webhook を作成
- GitHub の Secrets に `SLACK_WEBHOOK_URL` として Slack の Webhook URL を登録
  - 面倒であれば直接 `workflows/post-slack-message.yml` に書いても OK です
  - 補足：legacy な方の Webhook は未検証

3. 雑談の話題は ChatGPT に生成してもらったものをすでに入れてあるので、カスタマイズ不要でも使えます。追加したい場合は、お好みの雑談の話題を topics ディレクトリ配下に適当なファイルを作って、改行区切りで並べてください。`example-topics/` 配下に ChatGPT に出してもらったもの（5 分くらいの話題）を置いておくので、参考にしてみてください。

4. 雑談の話題を LLM に生成してもらうプロンプトを example-prompt.txt としておいてあるので、必要であれば使ってみてください。

