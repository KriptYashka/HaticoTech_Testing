from typing import List

from repositories.token import TokenRepository
from schemas.token import Token


class TokenService:
    def __init__(self, repository: TokenRepository) -> None:
        self.repository = repository

    def get_tokens(self) -> List[Token]:
        result = self.repository.get_tokens()
        return result

    def create_token(self) -> Token:
        result = self.repository.create_token()
        return result