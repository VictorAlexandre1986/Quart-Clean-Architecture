from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, Integer

Base = declarative_base(cls=AsyncAttrs)

class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255))
