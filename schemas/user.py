from pydantic import BaseModel

class SUser(BaseModel):
    username_tg: str
