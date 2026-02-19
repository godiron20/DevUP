
import telebot.types as types

# Начальные кнопки
startmarkup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('start')
itembtn2 = types.KeyboardButton('help')
startmarkup.add(itembtn1, itembtn2)

# Ответы на вопросы
markup = types.InlineKeyboardMarkup(row_width=1)
itembtn3 = types.InlineKeyboardButton('Набрать вес', callback_data='nabor')
itembtn4 = types.InlineKeyboardButton('Сбросить вес', callback_data='sbros')
markup.add(itembtn3, itembtn4)

racion_tren_markup = types.InlineKeyboardMarkup(row_width=2)
itembtn5 = types.InlineKeyboardButton('Какой у меня рацион?', callback_data='racion')
itembtn6 = types.InlineKeyboardButton('Какой у меня план тренировок?', callback_data='tren')
racion_tren_markup.add(itembtn5, itembtn6)