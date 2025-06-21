import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعدادات البوت
TOKEN = "8052278560:AAFgCDTxtQg2ngmfJK5LscJInaHYfez_uGM"
CHANNEL_USERNAME = "@marketeyeoptions"
ADMIN_CHAT_ID = 605473503  # معرّف حسابك في تيليجرام

WELCOME_TEXT = """مرحباً بك في بوت الاشتراك في قناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100%.

نقدم توصيات سكالبنق (Scalping) وسوينق (Swing)
مع سعر الدخول ووقف الخسارة ونوع العقد.

اضغط الزر أدناه للانضمام إلى القناة."""

# وظيفة حفظ الدخول في ملف log.json
def log_user(user_id, username, full_name, campaign):
    try:
        with open("log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if campaign not in data:
        data[campaign] = []

    if user_id not in [entry["id"] for entry in data[campaign]]:
        data[campaign].append({
            "id": user_id,
            "username": username,
            "name": full_name
        })

    with open("log.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    campaign = context.args[0] if context.args else "مسوق"

    # تسجيل المستخدم
    log_user(user.id, user.username, user.full_name, campaign)

    # إشعار لك برسالة خاصة
    message = f"""🆕 مستخدم جديد دخل البوت
👤 الاسم: {user.full_name}
🆔 يوزر: @{user.username if user.username else 'بدون يوزر'}
🎯 مصدر الدخول: {campaign}
"""
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)

    # إرسال رسالة الاشتراك مع زر الانضمام
    keyboard = [[InlineKeyboardButton("الانضمام إلى القناة", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# إعداد أوامر البوت
async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاشتراك في قناة عين السوق"),
        BotCommand("help", "شرح سريع حول استخدام البوت")
    ])

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).post_init(set_commands).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
