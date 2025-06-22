from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "8052278560:AAEGm-KcpLDFDAvzhW84MAlTQcUfwdql48Q"
ADMIN_ID = "@marketeyeoptions2"
CHANNEL_USERNAME = "@marketeyeoptions"

WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    ref_code = args[0] if args else "غير معروف"
    user = update.effective_user
    time_joined = datetime.now().strftime("%Y-%m-%d %H:%M")

    # إرسال رسالة ترحيب للمستخدم
    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

    # إرسال تنبيه إلى الأدمن
    msg = f"""📥 مستخدم جديد دخل عبر رابط المسوق

👤 الاسم: {user.full_name}
🔗 اسم المستخدم: @{user.username if user.username else 'لا يوجد'}
🕐 الوقت: {time_joined}
🏷 كود المسوق: {ref_code}
"""
    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في قناة عين السوق")
    ])

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.post_init = lambda app: set_commands(app)
    print("Bot is running...")
    app.run_polling()
