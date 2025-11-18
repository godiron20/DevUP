from config import settings
from telebot.async_telebot import AsyncTeleBot

token = settings.TELEGRAM_TOKEN
bot = None

def get_bot():
    global bot
    if bot is None:
        bot = AsyncTeleBot(token)
        print("Я выдал бота из None")
        return bot
    else:
        print("Я выдал бота")
        return bot
    
