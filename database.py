from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from orm import UserOrm, TokenOrm

engine = create_async_engine("sqlite+aiosqlite:///imei.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
   async with engine.begin() as conn:
      await conn.run_sync(UserOrm.metadata.create_all)
      await conn.run_sync(TokenOrm.metadata.create_all)


async def delete_tables():
   async with engine.begin() as conn:
      await conn.run_sync(UserOrm.metadata.drop_all)
      await conn.run_sync(TokenOrm.metadata.drop_all)