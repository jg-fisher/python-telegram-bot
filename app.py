from flask import Flask, request, jsonify

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    success = bot.action()
    return jsonify(success=success) # TODO: Success should reflect the success of the reply

if __name__ == '__main__':
    app.run(port=5000)


# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0>/getme
# check webhook url: https://api.telegram.org/bot822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0/getWebhookInfo