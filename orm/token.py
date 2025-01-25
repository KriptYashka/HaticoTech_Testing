from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Model(DeclarativeBase):
   pass

class TokenOrm(Model):
   __tablename__ = "token"
   id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
   username_tg: Mapped[str] = mapped_column()
   value: Mapped[str] = mapped_column(unique=True)