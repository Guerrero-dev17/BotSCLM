from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update: Update, context):
    update.message.reply_text("¡Hola! Soy un bot de ejemplo.")

def main():
    updater = Updater("TU_API_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
