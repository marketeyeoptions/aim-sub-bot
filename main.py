from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from datetime import datetime
import time

TOKEN = '8052278560:AAGAxKOYvHYjTFEVO5BiiMC_GkkiMds88rM'
CHANNEL_ID = '@marketeyeoptions1'

def is_market_open():
    now_utc = datetime.utcnow()
    return now_utc.hour >= 13 and now_utc.hour < 20

def forward_message(update: Update, context: CallbackContext):
    if is_market_open():
        if update.message.photo:
            photo = update.message.photo[-1].file_id
            caption = update.message.caption if update.message.caption else ""
            context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption)
        elif update.message.text:
            context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)
    else:
        update.message.reply_text("السوق غير مفتوح حالياً. أرسل التوصية بعد الساعة 4:30 مساءً بتوقيت السعودية.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text | Filters.photo, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
