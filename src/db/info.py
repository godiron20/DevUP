from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.schemas.info import UsersDB, TrenDB, TrenFilter, RacionDB, UsersUpdate
from src.models.info import Users, Tren, Racion
from src.db.session import get_session


async def create_user(body: UsersDB):
    async with get_session() as db_session:
        new_user = Users(**body.model_dump(exclude_unset=True))
        db_session.add(new_user)
        await db_session.commit()
        return new_user

async def update_user(body:UsersUpdate):
    async with get_session() as db_session:
        query = await db_session.execute(select(Users).where(Users.username == body.username))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)

async def get_users_list() -> list[UsersDB]:
    async with get_session() as db_session:
        query_result = await db_session.execute(select(Users))
        return query_result.scalars().all()
    
async def get_one(user_name:str):
    async with get_session() as db_session:
        query_result = await db_session.execute(select(Users).filter_by(username=user_name))
        return query_result.scalar_one_or_none()


async def create_tren(body: TrenDB):
    async with get_session() as db_session:
        new_tren = Tren(**body.model_dump(exclude_unset=True))
        db_session.add(new_tren)
        await db_session.commit()
        return new_tren

async def get_tren_list(filter:TrenFilter) -> list[TrenDB]:
    async with get_session() as db_session:

        query = select(Tren)

        if filter.limit != -1:
            query = query.limit(filter.limit)
        query = query.offset(filter.offset)

        if filter.group is not None:
            query = query.filter(Tren.group == filter.group)

        if filter.colvo_pod_from is not None:
            query = query.filter(Tren.colvo_pod >= filter.colvo_pod_from)
        if filter.colvo_pod_to is not None:
            query = query.filter(Tren.colvo_pod <= filter.colvo_pod_to)

        if filter.colvo_pov_from is not None:
            query = query.filter(Tren.colvo_pov >= filter.colvo_pov_from)
        if filter.colvo_pov_to is not None:
            query = query.filter(Tren.colvo_pov <= filter.colvo_pov_to)

        query_result = await db_session.execute(query)

        return query_result.scalars().all()



async def get_one(id: int):
    async with get_session() as db_session:
        query_result = await db_session.execute(select(Tren).filter_by(id = id))
        return query_result.scalar_one_or_none()
