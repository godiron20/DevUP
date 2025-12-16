
import telebot.types as types

# Начальные кнопки
startmarkup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('start')
itembtn2 = types.KeyboardButton('help')
startmarkup.add(itembtn1, itembtn2)

# Ответы на вопросы
markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn3 = types.KeyboardButton('Какой у тебя рост?')
itembtn4 = types.KeyboardButton('Сбросить вес')
markup.add(itembtn3, itembtn4)
