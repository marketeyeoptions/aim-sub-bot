from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"
CHANNEL_USERNAME = "@marketeyeoptions"
ADMIN_CHAT_ID = 605473503

WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    campaign = context.args[0] if context.args else "بدون حملة"

    message = f"""🆕 مستخدم دخل البوت
👤 الاسم: {user.full_name}
🆔 يوزر: @{user.username if user.username else 'بدون يوزر'}
🎯 الحملة: {campaign}
"""
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)

    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في قناة عين السوق"),
        BotCommand("help", "شرح سريع حول استخدام البوت")
    ])

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # تشغيل أوامر البوت بشكل آمن قبل polling
    import asyncio
    asyncio.run(set_commands(app))

    print("Bot is running...")
    app.run_polling()
