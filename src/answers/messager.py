import telebot.types as types
from src.conts.users import user_position
from src.answers.buttons import markup, startmarkup, racion_tren_markup
import json

from src.db.info import create_user, get_users_list, get_one
from src.schemas.info import UsersDB

from src.bot import get_bot

bot = None

lang = 'ru'
with open('answer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
lang_data = data[lang]

def init():
    global bot
    bot = get_bot()


    @bot.message_handler(commands=['start', 'help'])
    async def start_message(message):
        print(message.chat.id)
        await bot.reply_to(message, lang_data['Hello'])
        await bot.send_message(message.chat.id, lang_data["height"])
        user = UsersDB(
            id=message.from_user.id,
            username=message.from_user.username,
            lang=message.from_user.language_code,
            position=user_position.height
        )
        if not await get_one(message.from_user.username):
            await create_user(user)

    @bot.callback_query_handler(func=lambda callback: True)
    async def callback_message(callback):
        if callback.data == 'nabor':
            print('Hello world')



    # @bot.message_handler(commands=['reply_buttons'])
    # async def send_reply_keyboard(message: types.Message):
    #     await message.answer('Выберите кнопку:', reply_markup=startmarkup)


    # @bot.message_handler(func=lambda message: True)
    # async def echo_message(message):
    #     if message.text == lang_data["height"]:
    #         await bot.reply_to(message, "Соси хуй")
    #         # await bot.reply_to(message,str((await get_one(message.from_user.username)).__dict__))
    #     else:
    #         await bot.reply_to(message, "Соси хуй без веса")
