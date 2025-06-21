from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ التوكن الخاص بالبوت
TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"

# ✅ اسم قناة الاشتراك
CHANNEL_USERNAME = "@marketeyeoptions"

# ✅ معرف المسؤول (تلقاه من @userinfobot)
ADMIN_CHAT_ID = 605473503  # ← لا تحتاج تعديله، معرفك محفوظ

# ✅ رسالة الترحيب
WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

# ✅ تنفيذ أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    campaign = context.args[0] if context.args else "بدون حملة"

    message = f"""🆕 مستخدم دخل البوت
👤 الاسم: {user.full_name}
🆔 يوزر: @{user.username if user.username else 'بدون يوزر'}
🎯 الحملة: {campaign}
"""

    # إرسال تنبيه إلى المسؤول
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)

    # زر الانضمام للقناة
    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # الرد على المستخدم
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# ✅ ضبط أوامر البوت
async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في قناة عين السوق"),
        BotCommand("help", "شرح سريع حول استخدام البوت")
    ])

# ✅ تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.post_init = lambda app: set_commands(app)
    print("Bot is running...")
    app.run_polling()
