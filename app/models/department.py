from sqlalchemy.orm import Mapped

from app.models.base import Base, str_short


class Department(Base):
    __table__ = 'departments'
    name: Mapped[str_short]
