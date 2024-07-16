from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, str_short
from app.models.country import Country


class Region(Base):
    __tablename__ = 'regions'
    name: Mapped[str_short] = mapped_column(index=True)
    country_id: Mapped[int] = mapped_column(ForeignKey(Country.id), use_alter=True)
    country: Mapped[Country] = relationship(Country, back_populates='region')
