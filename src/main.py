import asyncio
import uvicorn

from src.bot import get_bot

from random import randint

from src.answers.messager import init as start_init
from src.conts.users import user_position
from src.db.info import create_user, get_users_list
from src.schemas.info import UsersDB
from src.config import settings


async def app():
    b = get_bot()

    start_init()

    await b.polling()
