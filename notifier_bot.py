import os, json
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

ADD_USER_API_URL = 'https://notifier-bot-api.herokuapp.com/User'

def start(update, context):
    payload = {
        "UserId": int(update.message.chat.id),
        "Username": str(update.message.chat.username),
        "FirstName": str(update.message.chat.first_name)
    }

    print(payload)

    response = requests.post(ADD_USER_API_URL,  data=json.dumps(payload), headers={"Content-Type":"application/json"})

    print(response.json())

    update.message.reply_text('Bienvenido...ahora puede recibir notificaciones de sus canales. Consulte la API https://notifier-bot-api.herokuapp.com/swagger')


def echo(update, context):
    update.message.reply_text('Mensaje recibido...')


def main():
    updater = Updater(os.environ['ACCESS_KEY'], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()