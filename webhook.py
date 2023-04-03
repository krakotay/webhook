import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TELEGRAM_API_KEY = ""
CHAT_ID = ""

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"Новый артефакт: {data['artifact_url']}"

    send_telegram_message(TELEGRAM_API_KEY, CHAT_ID, message)

    return jsonify({"status": "success"}), 200

def send_telegram_message(api_key, chat_id, message):
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response

if __name__ == "__main__":
    app.run()

