from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base, str_short
from app.models.region import Region


class Country(Base):
    __table__ = 'countries'
    name: Mapped[str_short]
    region: Mapped[Region] = relationship(Region, back_populates='country')
