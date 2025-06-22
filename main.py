from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توكن البوت
BOT_TOKEN = "8052278560:AAEGm-KcpLDFDAvzhW84MAlTQcUfwdql48Q"

# المعرّف الشخصي لحسابك اللي يستقبل التنبيهات (تأكد إنه @marketeyeoptions2)
ADMIN_USERNAME = "marketeyeoptions2"

# دالة start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # رسالة ترحيب للمستخدم
    await update.message.reply_text("مرحباً بك في قناة عين السوق 👁️📊\nشكراً لانضمامك!")

    # إرسال تنبيه لحساب الأدمن
    user = update.effective_user
    message = f"🔔 مستخدم جديد ضغط /start\nالاسم: {user.full_name}\nالمعرف: @{user.username or 'لا يوجد'}\nالمعرف الرقمي: {user.id}"
    
    # أرسل التنبيه إذا مشتركك معرفه معروف
    try:
        await context.bot.send_message(chat_id=f"@{ADMIN_USERNAME}", text=message)
    except Exception as e:
        print("خطأ في إرسال التنبيه:", e)

# إعداد البوت
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
