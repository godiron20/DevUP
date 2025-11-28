from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from schemas.users import UsersDB
from models.users import Users
from db.session import get_session


async def create_user(body: UsersDB):
    async with get_session() as db_session:
        new_user = Users(**body.model_dump(exclude_unset=True))
        db_session.add(new_user)
        await db_session.commit()
        return new_user

async def get_users_list() -> list[UsersDB]:
    async with get_session() as db_session:
        query_result = await db_session.execute(select(Users))
        return query_result.scalars().all()