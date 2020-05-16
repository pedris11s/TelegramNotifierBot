import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Welcome...')


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(os.environ['ACCESS_KEY'], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()