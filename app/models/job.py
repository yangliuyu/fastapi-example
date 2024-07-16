from datetime import datetime

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, long, str_short
from app.models.enums.language import Language


class Job(Base):
    __tablename__ = 'jobs'
    title: Mapped[str_short]
    min_salary: Mapped[long]
    max_salary: Mapped[long]


class JobHistory(Base):
    __tablename__ = 'job_histories'
    start_date: Mapped[datetime.date]
    end_date: Mapped[datetime.date]
    language: Mapped[Language] = mapped_column(Enum(Language))
