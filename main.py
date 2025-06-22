import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

# إعدادات التوكن والمعرف الذي يستقبل التنبيهات
BOT_TOKEN = "8052278560:AAEGm-KcpLDFDAvzhW84MAlTQcUfwdql48"
ADMIN_ID = 515795120  # حسابك الشخصي @marketeyeoptions2

# تفعيل اللوق
logging.basicConfig(level=logging.INFO)

# دالة الاستجابة لأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args  # قراءة كود المسوق (إن وُجد)
    code = args[0] if args else "بدون كود"

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = (
        f"📥 دخول جديد للبوت:\n"
        f"• الاسم: {user.full_name}\n"
        f"• المعرّف: @{user.username if user.username else 'بدون'}\n"
        f"• الوقت: {now}\n"
        f"• كود المسوق: {code}"
    )
    
    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

# تشغيل التطبيق
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
