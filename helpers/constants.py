import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Any


BASE_URL = 'https://qa-scooter.education-services.ru/'


class ButtonPlaces(Enum):
    BOTTOM = 'bottom'
    TOP = 'top'


@dataclass
class ClientData:
    def __init__(self, name, surname, address, station, phone, date, duration, color=None, comment=None):
        self.name = name
        self.surname = surname
        self.address = address
        self.station = station
        self.phone = phone
        self.date = date
        self.duration = duration
        self.color = color
        self.comment = comment


test_data_1 = ClientData(name="Василий",
                         surname="Чапаев",
                         address="Москва, проезд Девичьего Поля, 4",
                         station="Парк культуры",
                         phone="+71234567890",
                         date=(datetime.datetime.now() +
                               datetime.timedelta(days=1)).strftime('% d.%m.%Y'),
                         duration="пятеро суток",
                         color="чёрный жемчуг",
                         comment="зарядите до полной")

test_data_2 = ClientData(name="Илья",
                         surname="Ильф",
                         address="Москва, Лаврушинский переулок, дом 17",
                         station="Третьяковская",
                         phone="+79123456780",
                         date=(datetime.datetime.now() +
                               datetime.timedelta(days=1)).strftime('% d.%m.%Y'),
                         duration="двое суток",
                         color="серая безысходность")
