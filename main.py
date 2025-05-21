import time
import telegram

# توكن البوت الجديد
TOKEN = '8052278560:AAGAxKOYvHYjTFEVO5BiiMC_GkkiMds88rM'

# معرف القناة العامة
CHANNEL_ID = '@marketeyeoptions1'

# الرسالة الافتتاحية
START_MESSAGE = '''
تم تشغيل البوت بنجاح!

سيتم إرسال التوصيات والتحديثات تلقائيًا هنا.
#عين_السوق
'''

def main():
    bot = telegram.Bot(token=TOKEN)
    
    # إرسال أول رسالة عند التشغيل
    bot.send_message(chat_id=CHANNEL_ID, text=START_MESSAGE)
    
    # حلقة تشغيل دائمة (يمكنك إضافة منطق التوصيات داخلها لاحقًا)
    while True:
        time.sleep(60)

if __name__ == '__main__':
    main()
