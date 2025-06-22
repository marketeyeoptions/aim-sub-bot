from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

BOT_TOKEN = "8052278560:AAEGm-KcpLDFDAvzhW84MAlTQcUfwdql48Q"
ADMIN_USERNAME = "@marketeyeoptions2"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    username = update.effective_user.username or "بدون اسم مستخدم"
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if args:
        referral_code = args[0]
        message = f"👤 دخل شخص جديد للبوت\nالاسم: @{username}\nالوقت: {time}\nالمسوق: {referral_code}"
        await context.bot.send_message(chat_id=ADMIN_USERNAME, text=message)

    welcome_text = (
        "مرحباً بك في بوت الاشتراك الرسمي لقناة “عين السوق | توصيات أوبشن يومية”.\n\n"
        "الاشتراك مجاني 100٪.\n"
        "نقدم توصيات سكالبينق (Scalping) وويكلي (Swing)\n"
        "مع سعر الدخول ووقف الخسارة وتوزيع العقود.\n\n"
        "اضغط الزر أدناه للانضمام إلى القناة 👇"
    )
    join_button = [[
        {"text": "الانضمام إلى القناة 🟢", "url": "https://t.me/marketeyeoptions"}
    ]]
    await update.message.reply_text(welcome_text, reply_markup={"inline_keyboard": join_button})

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    import asyncio
    async def run():
        await app.bot.set_webhook("https://aim-sub-bot.onrender.com")
        await app.start()
        await app.updater.start_polling()
    asyncio.run(run())
