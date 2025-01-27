from typing import List

from repositories.token import TokenRepository
from schemas import SUser
from schemas.token import SToken


class TokenService:
    def __init__(self, repository: TokenRepository) -> None:
        self.repository = repository

    def get_token(self, _user: SUser) -> SToken:
        result = self.repository.get_token(_user.username_tg)
        return result

    def create_token(self, token: SToken) -> SToken:
        # TODO: Whitelist
        result = self.repository.create_token(token)
        return result
