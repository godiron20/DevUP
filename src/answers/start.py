import telebot.types as types
from answers.buttons import markup, startmarkup
import json

from bot import get_bot

bot = None

lang = 'ru'
with open('answer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
lang_data = data["lang_data"][lang]

def init():
    global bot
    bot = get_bot()

    @bot.message_handler(commands=['start', 'help'])
    async def start_message(message):
        print(message.chat.id)
        await bot.reply_to(message, lang_data['Hello'])
        await bot.send_message(message.chat.id, lang_data["2mes"], reply_markup=markup)

    @bot.message_handler(commands=['reply_buttons'])
    async def send_reply_keyboard(message: types.Message):
        await message.answer('Выберите кнопку:', reply_markup=startmarkup)

    @bot.message_handler(content_types=['photo'])
    async def start_message(message):
        await bot.send_photo(message.chat.id, message.photo[0].file_id, reply_markup = startmarkup)
        await bot.send_message(message.chat.id, 'ヾ(•ω•`)o')

    @bot.message_handler(func=lambda message: True)
    async def echo_message(message):
        if message.text == lang_data["mas"]:
            await bot.reply_to(message, "Соси хуй")
        else:
            await bot.reply_to(message, "Соси хуй без веса")
