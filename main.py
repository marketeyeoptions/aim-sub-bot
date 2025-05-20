from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8052278560:AAGAxKOYvHYjTFEVO5BiiMC_GkkiMds88rM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url="https://t.me/marketeyeoptions")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "**مرحبًا بك في بوت الاشتراك الرسمي لقناة عين السوق | توصيات أوبشن يومية**\n\n"
        "للوصول إلى التوصيات اليومية:\n"
        "1. تأكد أنك اشتركت في القناة.\n"
        "2. اضغط الزر أدناه للانضمام الآن.\n\n👇👇👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
