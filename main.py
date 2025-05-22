import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"
CHANNEL_USERNAME = "@marketeyeoptions"  # اسم قناة عين السوق (تأكد من صحته)

# رسالة البداية
WELCOME_TEXT = """مرحباً بك في بوت الاشتراك الخاص بقناة "عين السوق | توصيات أوبشن يومية".

اضغط الزر أدناه للانضمام إلى القناة ومتابعة التوصيات أولاً بأول.
"""

# دالة الاستجابة لأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
