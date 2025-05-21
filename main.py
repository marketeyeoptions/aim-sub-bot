import time
import telegram
from datetime import datetime

# إعدادات البوت
TOKEN = '8052278560:AAGAxKOYvHYjTFEVO5BiiMC_GkkiMds88rM'
CHANNEL_ID = '@marketeyeoptions1'

def is_market_open():
    now_utc = datetime.utcnow()
    # السوق من 13:30 إلى 20:00 بتوقيت UTC (يعادل 4:30م - 11:00م بتوقيت السعودية)
    return now_utc.hour >= 13 and (now_utc.hour < 20 or (now_utc.hour == 20 and now_utc.minute == 0))

def main():
    bot = telegram.Bot(token=TOKEN)
    sent_start = False  # لتفادي التكرار

    while True:
        if is_market_open():
            if not sent_start:
                bot.send_message(chat_id=CHANNEL_ID, text="البوت شغّال الآن وقت التداول.")
                sent_start = True

            # مكان إضافة منطق التوصيات أو الاستقبال
            time.sleep(10)  # راقب كل 10 ثواني مثلاً

        else:
            if sent_start:
                bot.send_message(chat_id=CHANNEL_ID, text="انتهى وقت التداول. البوت سيعود غدًا.")
                sent_start = False

            # نام حتى يبدأ السوق (راجع كل 10 دقائق فقط خارج وقت السوق)
            time.sleep(600)

if __name__ == '__main__':
    main()
