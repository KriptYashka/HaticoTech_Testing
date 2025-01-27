from typing import List
from typing import List
from sqlalchemy import select, update, delete, CursorResult
from database import new_session
from orm import TokenOrm
from schemas.token import SToken

class TokenRepository:
    @classmethod
    async def create_token(cls, token: SToken) -> SToken:
        async with new_session() as session:
            session.add(token)
            await session.flush()
            await session.commit()
            return token


    @classmethod
    async def get_token(cls, username_tg: str) -> TokenOrm:
        async with new_session() as session:
            query = select(TokenOrm).where(TokenOrm.username_tg == username_tg)
            result = await session.execute(query)
            token = result.scalars().first()
            return token


    @classmethod
    async def delete_token(cls, username_tg: str):
        async with new_session() as session:
            query = delete(TokenOrm).where(TokenOrm.username_tg == username_tg)
            result: CursorResult = await session.execute(query)
            await session.commit()
            return result