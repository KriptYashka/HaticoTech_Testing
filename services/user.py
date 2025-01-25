from typing import List

from repositories.user import UserRepository
from schemas.user import User


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get_tokens(self) -> List[User]:
        result = self.repository.get_tokens()
        return result

    def create_token(self) -> User:
        result = self.repository.create_token()
        return result