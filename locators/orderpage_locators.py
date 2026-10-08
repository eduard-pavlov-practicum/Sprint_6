from selenium.webdriver.common.by import By

from helpers.constants import ButtonPlaces


NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
ADDRESS_INPUT = (
    By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
PHONE_INPUT = (
    By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
RENT_DURATION_DROPDOWN = (By.XPATH, '//input[@placeholder="* Срок аренды"]')
RENT_DURATION_OPTIONS = (
    By.XPATH, '//div[text()="* Срок аренды"]/parent::div/parent::div[contains(@class, "Dropdown-root") and contains(@class,"is-open")]/div[@class="Dropdown-menu"]/div[@class="Dropdown-option"]')
# COLOR_BLACK = (By.XPATH, '//div[text()="Цвет самоката"]/parent::div/label[text()="чёрный жемчуг"]')
# COLOR_GREY = (By.XPATH, '//div[text()="Цвет самоката"]/parent::div/label[text()="серая безысходность"]')
SCOOTER_COLOR_TEMPLATE = (
    By.XPATH, '//div[text()="Цвет самоката"]/parent::div/label[text()="{}"]')
COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
YES_BUTTON = (
    By.XPATH, '//div[text()="Хотите оформить заказ?"]/following-sibling::div/button[text()="Да"]')
SHOW_STATUS_BUTTON = (
    By.XPATH, '//div[starts-with(text(),"Заказ оформлен")]/following-sibling::div/button[text()="Посмотреть статус"]')
