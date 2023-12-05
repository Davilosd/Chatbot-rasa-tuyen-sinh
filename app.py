from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()
    print("Rasa Response:", rasa_response_json)
    bot_responses = []
    for response in rasa_response_json:
        bot_responses.append(response.get('text', ''))
    if not rasa_response_json:
        bot_responses.append('Xin lỗi, tôi chưa rõ ý của bạn là gì. Dưới đây là một số câu hỏi khác mà bạn có thể sử dụng <><> updating...')
    return jsonify({'response': bot_responses})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    