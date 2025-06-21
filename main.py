from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"
CHANNEL_USERNAME = "@marketeyeoptions"

WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # ضبط الأوامر
    await app.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في قناة عين السوق"),
        BotCommand("help", "شرح سريع حول استخدام البوت")
    ])

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
