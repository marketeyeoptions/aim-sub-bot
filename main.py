import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

# بيانات البوت
BOT_TOKEN = "8052278560:AAFRVJPAq9LOXNwzpiB3bKSi5DwlWDbBCSo"
ADMIN_USERNAME = "@marketeyeoptions2"  # الحساب الذي تصله التنبيهات

# تفعيل السجل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# دالة أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ref_code = context.args[0] if context.args else "غير محدد"
    username = user.username or "بدون اسم"
    name = user.first_name or ""
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # إرسال رسالة ترحيب للمستخدم
    await update.message.reply_text(
        "مرحبًا بك في بوت الاشتراك الرسمي لقناة “عين السوق | توصيات أوبشن يومية”.\n\n"
        "📢 الاشتراك مجاني 100%\n"
        "🤖 نقدم توصيات سكالبينق (Scalping) وسوينق (Swing)\n"
        "📈 مع سعر الدخول ووقف الخسارة ونقطة الهدف.\n\n"
        "👇 اضغط الزر أدناه للانضمام إلى القناة:\n"
        "https://t.me/marketeyeoptions"
    )

    # إرسال تنبيه للإدارة
    alert_message = (
        "🚨 دخول جديد عبر رابط الإحالة:\n"
        f"• الاسم: {name}\n"
        f"• اسم المستخدم: @{username}\n"
        f"• الوقت: {time_now}\n"
        f"• كود المسوق: {ref_code}"
    )

    await context.bot.send_message(chat_id=ADMIN_USERNAME, text=alert_message)

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
