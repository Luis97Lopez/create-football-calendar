from pydantic import BaseModel, BeforeValidator, AfterValidator
from datetime import date, time, datetime, timezone
from typing import Annotated
from zoneinfo import ZoneInfo


def timezone_time(value: time):
    print(value)
    value = value.replace(tzinfo=ZoneInfo("America/Mexico_City"))
    print(value)
    return value


def create_date(value):
    try:
        return datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError:
        return datetime.strptime(value, "%Y/%m/%d").date()


class Partido(BaseModel):
    clubLocal: str
    clubVisita: str
    division: str
    temporada: str
    torneo: str
    numeroJornada: str
    fecha103: Annotated[date, BeforeValidator(create_date)]
    Hora: Annotated[time, AfterValidator(timezone_time)]
    estadio: str
    CanaldeTV: str
