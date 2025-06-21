from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"
CHANNEL_ID = -1002143952381  # قناة: @marketeyeoptions

WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    tag = args[0] if args else "بدون كود"

    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url="https://t.me/marketeyeoptions")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

    name = user.full_name
    username = f"@{user.username}" if user.username else "لا يوجد"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = f"""🚨 تم دخول مستخدم جديد عن طريق المسوق:

الاسم: {name}
المعرف: {username}
الوقت: {now}
رمز المسوق: {tag}
"""
    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg)

async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في القناة")
    ])

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.post_init = lambda app: set_commands(app)
    app.run_polling()
