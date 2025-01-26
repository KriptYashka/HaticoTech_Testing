from pydantic import BaseModel

class SToken(BaseModel):
    id: int
    username_tg: str
    value: str
