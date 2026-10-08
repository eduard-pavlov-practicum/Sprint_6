import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from locators import orderpage_locators as locators
from pages.base_page import BasePage
from helpers.constants import ButtonPlaces, ClientData


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = locators

    def find_name_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.NAME_INPUT)

    def find_surname_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.SURNAME_INPUT)

    def find_address_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.ADDRESS_INPUT)

    def find_station_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.STATION_INPUT)

    def find_phone_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.PHONE_INPUT)

    def find_next_button(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.NEXT_BUTTON)

    def fill_value_into_input_element(self, element: WebElement, value: str):
        element.send_keys(value)

    def find_date_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.DATE_INPUT)

    def find_duration_dropdown(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.RENT_DURATION_DROPDOWN)

    def find_color_checkbox(self, color: str) -> WebElement:
        color_locator = (self.locators.SCOOTER_COLOR_TEMPLATE[0],
                         self.locators.SCOOTER_COLOR_TEMPLATE[1].format(color))
        return self.find_element_with_scroll(color_locator)

    def find_comment_input(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.COMMENT_INPUT)

    def find_order_button(self) -> WebElement:
        return self.find_element_with_scroll(self.locators.ORDER_BUTTON)

    def select_duration_option(self, duration: str):
        dropdown_options: list[WebElement] = self.driver.find_elements(
            *self.locators.RENT_DURATION_OPTIONS)
        self.wait_element_visible(dropdown_options[0])
        for option in dropdown_options:
            if option.text == duration:
                self.wait_element_clickable(option)
                self.click_element(option)
                break

    @allure.step('Заполняем форму заказа для {client_data.name} {client_data.surname}')
    def make_order(self, client_data: ClientData) -> None:
        self.fill_value_into_input_element(
            self.find_name_input(), client_data.name)
        self.fill_value_into_input_element(
            self.find_surname_input(), client_data.surname)
        self.fill_value_into_input_element(
            self.find_address_input(), client_data.address)
        self.fill_value_into_input_element(
            self.find_station_input(), client_data.station)
        self.fill_value_into_input_element(
            self.find_phone_input(), client_data.phone)

        self.click_element(self.find_next_button())

    @allure.step('Заполняем параметры аренды: дата {date}, срок "{duration}", цвет {color}')
    def fill_rent_details(self, date: str, duration: str, color: str, comment: str = "") -> None:
        date_field = self.find_date_input()
        self.fill_value_into_input_element(date_field, date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(self.find_duration_dropdown())
        self.select_duration_option(duration)

        self.click_element(self.find_color_checkbox(color))

        self.fill_value_into_input_element(self.find_comment_input(), comment)

        self.click_element(self.find_order_button())

    @allure.step('Закрываем модальные окна')
    def close_confirmations(self):
        self.click_element(self.find_element_with_scroll(
            self.locators.YES_BUTTON))

        self.click_element(self.find_element_with_scroll(
            self.locators.SHOW_STATUS_BUTTON))
