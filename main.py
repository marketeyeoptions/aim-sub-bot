from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import logging

# ✅ توكن البوت (لا تغيّره إذا هو شغال عندك)
TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"
CHANNEL_USERNAME = "@marketeyeoptions"  # رابط القناة بدون تعديل

# ⚙️ ملف لتخزين الاشتراكات
SUB_FILE = "subs.txt"

# 🔧 تهيئة تسجيل الأحداث
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# 📩 نص الترحيب
WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100٪.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

# ▶️ أمر /start مع تتبع رابط المسوق
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    ref = args[0] if args else "مباشر"

    # 💾 تسجيل الدخول في ملف subs.txt
    with open(SUB_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - @{user.username or 'بدون_يوزر'} - من: {ref}\n")

    # 🔘 زر الانضمام للقناة
    keyboard = [
        [InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# 🛠️ إعداد الأوامر
async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في قناة عين السوق")
    ])

# 🟢 تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.post_init = lambda app: set_commands(app)
    print("Bot is running...")
    app.run_polling()
