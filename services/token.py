from typing import List

from repositories.token import TokenRepository
from schemas.token import SToken


class TokenService:
    def __init__(self, repository: TokenRepository) -> None:
        self.repository = repository

    def get_tokens(self) -> List[SToken]:
        result = self.repository.get_tokens()
        return result

    def create_token(self) -> SToken:
        result = self.repository.create_token()
        return result
