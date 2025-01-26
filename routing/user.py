from typing import List

from fastapi import APIRouter, Depends

from depends import get_user_service
from schemas import SUser
from services import UserService

router = APIRouter(prefix="/api/user", tags=["user"])

@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[SUser],
   description="Получение всех пользователей",
)
async def get_all_users(
       user_service: UserService = Depends(get_user_service),
) -> List[SUser]:
   users = await user_service.get_users()
   return users

@router.post(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=SUser,
   description="Создание пользователей",
)
async def create_user(
       _user: SUser,
       user_service: UserService = Depends(get_user_service),
) -> SUser:
   user = await user_service.create_user(_user)
   return user
