from datetime import datetime

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, long, str_short


class Employee(Base):
    __tablename__ = 'employees'
    first_name: Mapped[str_short]
    last_name: Mapped[str_short]
    email: Mapped[str_short]
    phone_number: Mapped[str_short]
    hire_date: Mapped[datetime.date] = mapped_column(Date)
    salary: Mapped[long]
    commission_pct: Mapped[long]
