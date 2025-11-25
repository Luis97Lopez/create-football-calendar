import json
from ics import Calendar, Event
from schema import Partido
from pprint import pprint
from datetime import datetime, timedelta


def json_to_ics(json_data, output_file):
    """
    Convierte un JSON a un archivo ICS.

    Args:
    - json_data: Diccionario con la estructura del evento.
    - output_file: Nombre del archivo ICS a generar.
    """
    calendar = Calendar()

    for event_data in json_data["events"]:
        partido = Partido(**event_data)
        event_begin = datetime.combine(partido.fecha103, partido.Hora)
        event_end = event_begin + timedelta(hours=2)
        event = Event()
        event.name = f"{partido.clubLocal} vs {partido.clubVisita}"
        event.begin = event_begin
        event.end = event_end
        event.description = f"J{partido.numeroJornada} - {partido.CanaldeTV}"
        event.location = partido.estadio

        calendar.events.add(event)

    with open(output_file, "w") as f:
        f.writelines(calendar)


with open("./matches.json", "r") as f:
    data = json.load(f)

# Crear un archivo ICS
json_to_ics(data, "output.ics")
