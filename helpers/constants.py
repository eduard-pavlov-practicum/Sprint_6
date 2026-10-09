import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Any


BASE_URL = 'https://qa-scooter.education-services.ru/'
YA_URL = 'https://ya.ru/'

QUESTIONS = [
    ('Сколько это стоит? И как оплатить?',
     'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    ('Хочу сразу несколько самокатов! Так можно?',
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    ('Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    ('Можно ли заказать самокат прямо на сегодня?',
     'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    ('Можно ли продлить заказ или вернуть самокат раньше?',
     'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    ('Вы привозите зарядку вместе с самокатом?',
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    ('Можно ли отменить заказ?',
     'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    ('Я жизу за МКАДом, привезёте?',
     'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]


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

    def __repr__(self) -> str:
        return f"ClientData(name={self.name}, surname={self.surname})"


test_data_1 = ClientData(name="Василий",
                         surname="Чапаев",
                         address="Москва, проезд Девичьего Поля, 4",
                         station="Парк культуры",
                         phone="+71234567890",
                         date=(datetime.datetime.now() +
                               datetime.timedelta(days=1)).strftime('%d.%m.%Y'),
                         duration="пятеро суток",
                         color="чёрный жемчуг",
                         comment="зарядите до полной")

test_data_2 = ClientData(name="Илья",
                         surname="Ильф",
                         address="Москва, Лаврушинский переулок, дом 17",
                         station="Третьяковская",
                         phone="+79123456780",
                         date=(datetime.datetime.now() +
                               datetime.timedelta(days=1)).strftime('%d.%m.%Y'),
                         duration="двое суток",
                         color="серая безысходность")
