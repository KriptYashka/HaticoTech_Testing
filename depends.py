"""
Файл внедрения зависимостей
"""
from repositories import TokenRepository, UserRepository
from services import TokenService, UserService

token_repository = TokenRepository()
token_service = TokenService(token_repository)

user_repository = UserRepository()
user_service = UserService(user_repository)

def get_token_service() -> TokenService:
   return token_service

def get_user_service() -> UserService:
   return user_service