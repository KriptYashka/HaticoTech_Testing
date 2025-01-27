from typing import List

from fastapi import APIRouter, Depends

from depends import get_token_service
from schemas import SUser, SToken
from services import TokenService

router = APIRouter(prefix="/api/token", tags=["token"])

@router.get(
    ""
)
async def get_token(
    _user: SUser,
    token_service: TokenService = Depends(get_token_service),
):
    token = await token_service.get_token(_user)
    return token

@router.post(
    ""
)
async def post_token(
    _token: SToken,
    token_service: TokenService = Depends(get_token_service),
):
    result = await token_service.create_token(_token)
    return result