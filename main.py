from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# بيانات البوت
TOKEN = '8052278560:AAGAxKOYvHYjTFEVO5BiiMC_GkkiMds88rM'
CHANNEL_ID = '@marketeyeoptions1'  # غيّرها إذا تغيّر اسم القناة

# الدالة الأساسية للتعامل مع كل الرسائل
def forward_message(update: Update, context: CallbackContext):
    message = update.message

    # إذا كانت الرسالة تحتوي صورة
    if message.photo:
        photo = message.photo[-1].file_id  # أعلى دقة
        caption = message.caption if message.caption else ""
        context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption)

    # إذا كانت الرسالة نص فقط
    elif message.text:
        context.bot.send_message(chat_id=CHANNEL_ID, text=message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # التقاط جميع الصور والنصوص
    dp.add_handler(MessageHandler(Filters.photo | Filters.text, forward_message))

    # تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
