from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime

# توكن البوت (استبدله بالتوكن الحقيقي)
BOT_TOKEN = "8052278560:AAEGm-KcpLDFDAvzhW84MAlTQcUfwdql48Q"

# معرف الحساب الذي يستقبل تنبيهات الدخول (مع @)
OWNER_USERNAME = "@marketeyeoptions2"

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # التحقق من وجود كود المسوق
    args = context.args
    if args:
        referral_code = args[0]
        message = (
            f"👤 مستخدم جديد دخل البوت\n"
            f"الاسم: {user.full_name}\n"
            f"المعرف: @{user.username}\n"
            f"الوقت: {time}\n"
            f"كود المسوق: {referral_code}"
        )
        await context.bot.send_message(chat_id=OWNER_USERNAME, text=message)

    # رسالة الترحيب
    keyboard = [[InlineKeyboardButton("🟢 الانضمام إلى القناة", url="https://t.me/marketeyeoptions")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "مرحباً بك في بوت الاشتراك الرسمي لقناة “عين السوق | توصيات أوبشن يومية”.\n\n"
        "الاشتراك مجاني 100٪.\n"
        "نقدم توصيات سكالبينق (Scalping) وويكلي (Swing)\n"
        "مع سعر الدخول ووقف الخسارة وتوزيع العقود.\n\n"
        "اضغط الزر أدناه للانضمام إلى القناة 👇",
        reply_markup=reply_markup
    )

# تهيئة وتشغيل البوت
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
