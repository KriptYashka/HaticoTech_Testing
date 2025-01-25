from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Model(DeclarativeBase):
   pass

class UserOrm(Model):
   __tablename__ = "user"
   username_tg: Mapped[str] = mapped_column(primary_key=True, unique=True)