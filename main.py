from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
from datetime import datetime

# إعدادات
BOT_TOKEN = "8052278560:AAEGm-KcpLDFDAvzhW84MAlTQcUfwdql48Q"
ADMIN_USERNAME = "@marketeyeoptions2"  # الحساب الذي يصله التنبيه

# إعدادات اللوق
logging.basicConfig(level=logging.INFO)

# دالة الرد على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.full_name
    username = f"@{user.username}" if user.username else "بدون اسم مستخدم"
    user_id = user.id
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # قراءة كود الإحالة إن وُجد
    args = context.args
    referral = args[0] if args else "لا يوجد"

    # إرسال الرسالة للمستخدم
    welcome_message = (
        "مرحباً بك في بوت الاشتراك الرسمي لقناة “عين السوق | توصيات أوبشن يومية”.\n\n"
        "الاشتراك مجاني 100٪:\n"
        "نقدم توصيات سكالبينق (Scalping) وويكلـي (Swing)\n"
        "مع سعر الدخول ووقف الخسارة وتوزيع العقود.\n\n"
        "اضغط الزر أدناه للانضمام إلى القناة 👇"
    )
    join_button = [["الانضمام إلى القناة 🟢", "https://t.me/marketeyeoptions"]]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/marketeyeoptions")

    # إرسال التنبيه لحساب الأدمن
    admin_alert = (
        f"🚨 دخول جديد إلى البوت\n\n"
        f"👤 الاسم: {user_name}\n"
        f"💬 يوزر: {username}\n"
        f"🆔 ID: {user_id}\n"
        f"⏰ الوقت: {time_now}\n"
        f"🏷️ كود الإحالة: {referral}"
    )
    await context.bot.send_message(chat_id=ADMIN_USERNAME, text=admin_alert)

# تشغيل البوت
if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
