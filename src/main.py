import asyncio

from bot import get_bot

from random import randint

from answers.start import init as start_init
from conts.users import user_position
from db.user import create_user, get_users_list
from schemas.users import UsersDB
from config import settings

asyncio.run(create_user(UsersDB(id=randint(-1000,1000), name='JOE', lang='38r904390-34598029.ру',calories=1000,position=user_position.my_colories), ))
t = asyncio.run(get_users_list())
for i in t:
    print(i.__dict__)

b = get_bot()

start_init()


asyncio.run(b.polling())


# Сначала мы вводим что нам требуется в плане программы, нам должны вывести универсальный план тренировок
# После этого бот хочет узнать что нам требуется набрать или сбросить, дальше бот узнаёт количество каллорий для нас и выдаёт в определённом диапозоне рацион питания подстроенный для нас.
