from sqlalchemy.orm import Mapped

from app.models.base import Base, str_long, str_short


class Location(Base):
    __tablename__ = 'locations'
    street_address: Mapped[str_long]
    postal_code: Mapped[str_short]
    city: Mapped[str_short]
    province: Mapped[str_long]
