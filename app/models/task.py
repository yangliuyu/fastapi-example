from sqlalchemy.orm import Mapped

from app.models.base import Base, str_long, str_short


class Task(Base):
    __table__ = 'tasks'
    title: Mapped[str_short]
    description: Mapped[str_long]
