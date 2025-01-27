from typing import List

from repositories.user import UserRepository
from schemas.user import SUser


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def get_users(self) -> List[SUser]:
        result = await self.repository.get_users()
        return result

    async def create_user(self, _user: SUser) -> SUser:
        result = await self.repository.create_user(_user)
        return result

    async def delete_user(self, _user: SUser) -> SUser:
        result = await self.repository.delete_user(_user.username_tg)
        return result