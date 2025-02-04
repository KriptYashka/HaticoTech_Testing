from typing import List
from sqlalchemy import select, update, delete, CursorResult
import logging

from orm.user import UserOrm
from database import new_session
from schemas import SUser


class UserRepository:
    @classmethod
    async def create_user(cls, user: SUser) -> UserOrm:
        async with new_session() as session:
            data = user.model_dump()
            new_user = UserOrm(**data)
            session.add(new_user)
            await session.flush()
            await session.commit()
            return new_user

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            users_models = result.scalars().all()
            users = [user_model for user_model in users_models]
            return users


    @classmethod
    async def get_user(cls, username_tg: int) -> UserOrm:
        async with new_session() as session:
            query = select(UserOrm).where(UserOrm.username_tg == username_tg)
            result = await session.execute(query)
            user = result.scalars().first()
            return user


    @classmethod
    async def delete_user(cls, username_tg: str):
        async with new_session() as session:
            query = delete(UserOrm).where(UserOrm.username_tg == username_tg)
            result: CursorResult = await session.execute(query)
            await session.commit()
            return result
