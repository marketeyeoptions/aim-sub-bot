import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن الجديد للبوت
TOKEN = "8052278560:AAFRVJPAq9LOXNwzpiB3bKSi5DwlWDbBCSo"

# آيدي الأدمن اللي توصله التنبيهات
ADMIN_CHAT_ID = 5041169546

# رسالة ترحيب
WELCOME_MSG = """مرحبًا بك في بوت الاشتراك الرسمي لقناة "عين السوق | توصيات أوبشن يومية".

الاشتراك مجاني 100٪.

نقدم توصيات سكالبينق (Scalping) وويكلي (Swing)
مع سعر الدخول ووقف الخسارة وتوزيع العقود.

اضغط الزر أدناه للانضمام إلى القناة 👇
"""

# عند الضغط على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username or "بدون اسم مستخدم"
    first_name = user.first_name or ""

    # استخراج كود المسوق إن وجد
    code = context.args[0] if context.args else "غير محدد"

    # إرسال رسالة ترحيب للمستخدم
    await update.message.reply_text(WELCOME_MSG)
    await update.message.reply_text(
        "🟢 [الانضمام إلى القناة](https://t.me/marketeyeoptions)", parse_mode="Markdown"
    )

    # إرسال تنبيه للأدمن
    msg = f"""🟢 دخل مستخدم جديد إلى البوت:

• الاسم: {first_name}
• المستخدم: @{username}
• الكود: {code}
"""
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

# إعداد البوت
def main():
    logging.basicConfig(level=logging.INFO)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
