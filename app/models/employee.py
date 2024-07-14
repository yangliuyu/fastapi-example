from datetime import datetime

from sqlalchemy.orm import Mapped

from app.models.base import Base, long, str_short


class Employee(Base):
    __table__ = 'employees'
    first_name: Mapped[str_short]
    last_name: Mapped[str_short]
    email: Mapped[str_short]
    phone_number: Mapped[str_short]
    hire_date: Mapped[datetime.date]
    salary: Mapped[long]
    commission_pct: Mapped[long]
