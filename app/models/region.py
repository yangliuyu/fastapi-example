from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, str_short


class Region(Base):
    __tablename__ = 'regions'
    name: Mapped[str_short] = mapped_column(index=True)
    country_id: Mapped[int] = mapped_column("countries.id", use_alter=True)
    country = relationship("Country", back_populates='region')
