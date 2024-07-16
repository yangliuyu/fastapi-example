import datetime

from sqlalchemy import BIGINT, JSON, String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column
from typing_extensions import Annotated

int_pk = Annotated[int, mapped_column(BIGINT, init=False, primary_key=True)]

long = Annotated[int, mapped_column(BIGINT)]

user_id = Annotated[int, mapped_column(BIGINT)]

date_auto = Annotated[datetime.date, mapped_column(init=False, default=datetime.date.today)]

timestamp_auto = Annotated[
    datetime.datetime, mapped_column(init=False, default=datetime.datetime.utcnow)
]

str_short = Annotated[str, mapped_column(String(127))]

str_long = Annotated[str, mapped_column(String(255))]

json_data = Annotated[dict, mapped_column(JSON)]


class Base(MappedAsDataclass, DeclarativeBase):
    id: Mapped[int_pk]
    created_at: Mapped[timestamp_auto]
    created_by: Mapped[user_id]
    updated_at: Mapped[timestamp_auto]
    updated_by: Mapped[user_id]
