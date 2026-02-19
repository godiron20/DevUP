from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base

from src.conts.users import user_position


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(String, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=True)
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    imt: Mapped[float] = mapped_column(Float, nullable=True)
    lang: Mapped[str] = mapped_column(String, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=True)
    position: Mapped[user_position] = mapped_column(String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False)


class Tren(Base):
    __tablename__ = 'tren'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group: Mapped[str] = mapped_column(String, nullable=False)
    colvo_pod: Mapped[str] = mapped_column(String, nullable=False)
    colvo_pov: Mapped[str] = mapped_column(String, nullable=False)


class Racion(Base):
    __tablename__ = 'racion'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    vid: Mapped[str] = mapped_column(String, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    ygli: Mapped[float] = mapped_column(Float, nullable=False)
    fats: Mapped[float] = mapped_column(Float, nullable=False)
    belki: Mapped[float] = mapped_column(Float, nullable=False)
