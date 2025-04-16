# bot.py
import telegram
from config import BOT_TOKEN, USER_ID

bot = telegram.Bot(token=BOT_TOKEN)

def send_signal(message):
    bot.send_message(chat_id=USER_ID, text=message)
