from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base, str_short


class Country(Base):
    __tablename__ = 'countries'
    name: Mapped[str_short]
    region: Mapped["Region"] = relationship("Region", back_populates='country')
