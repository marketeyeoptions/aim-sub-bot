from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

TOKEN = "توكن_البوت_هنا"
CHANNEL_USERNAME = "@marketeyeoptions"

# إعدادات اللوق
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    user = update.effective_user.first_name

    if "?ref=مسوق" in message_text:
        logging.info(f"🟢 مشترك جديد من رابط المسوق: {user}")
    else:
        logging.info(f"🟢 مشترك جديد بدون رابط إحالة: {user}")

    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
