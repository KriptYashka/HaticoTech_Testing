"""
Файл внедрения зависимостей
"""
from repositories.token import TokenRepository
from services.token import TokenService

token_repository = TokenRepository()
token_service = TokenService(token_repository)

def get_token_service() -> TokenService:
   return token_service