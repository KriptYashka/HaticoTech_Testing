from typing import List

from fastapi import APIRouter, Depends

from depends import get_token_service
from schemas.token import Token
from services.token import TokenService

router = APIRouter(prefix="/api/user", tags=["user"])

