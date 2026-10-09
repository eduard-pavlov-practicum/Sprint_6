import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from locators import orderpage_locators as locators
from pages.base_page import BasePage
from helpers.constants import ClientData


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
        dropdown_options = self.driver.find_elements(
            *self.locators.RENT_DURATION_OPTIONS)
        self.wait_element_visible(dropdown_options[0])
        for option in dropdown_options:
            if option.text == duration:
                self.click_element(self.wait_element_clickable(option))
                break

    def select_station(self, station):
        station_item_locator = (self.locators.STATION_ITEM_TEMPLATE[0],
                                self.locators.STATION_ITEM_TEMPLATE[1].format(station))
        return self.find_element_with_scroll(station_item_locator)

    @allure.step('Заполняем форму заказа для {client_data}')
    def make_order(self, client_data: ClientData) -> None:
        self.fill_value_into_input_element(
            self.find_name_input(), client_data.name)
        self.fill_value_into_input_element(
            self.find_surname_input(), client_data.surname)
        self.fill_value_into_input_element(
            self.find_address_input(), client_data.address)
        station_input = self.find_station_input()
        self.fill_value_into_input_element(
            station_input, client_data.station)
        self.click_element(self.select_station(client_data.station))
        self.fill_value_into_input_element(
            self.find_phone_input(), client_data.phone)

        self.click_element(self.find_next_button())

    @allure.step('Заполняем параметры аренды')
    def fill_rent_details(self, client_data: ClientData) -> None:
        date_field = self.find_date_input()
        self.fill_value_into_input_element(date_field, client_data.date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(self.find_duration_dropdown())
        self.select_duration_option(client_data.duration)

        # поля цвет и коментарий необязательны и могут быть не переданы
        if client_data.color:
            self.click_element(self.find_color_checkbox(client_data.color))

        if client_data.comment:
            self.fill_value_into_input_element(
                self.find_comment_input(), client_data.comment)

        self.click_element(self.find_order_button())

    @allure.step('Закрываем модальное окно "вы уверены"')
    def close_are_you_sure_modal(self):
        modal_view = self.wait_element_visible(self.find_element_with_scroll(
            self.locators.ARE_YOU_SHURE_MODAL))
        self.click_element(self.wait_element_clickable(self.find_element_in_block(modal_view,
                                                                                  self.locators.YES_BUTTON)))

    @allure.step('Получаем и закрываем модальное окно подтверждения')
    def get_confirmation_modal_view_text(self):
        modal_view = self.wait_element_visible(self.find_element_with_scroll(
            self.locators.CONFIRMATION_MODAL))
        text = modal_view.text
        if modal_view:
            self.click_element(self.find_element_in_block(modal_view,
                                                          self.locators.SHOW_STATUS_BUTTON))
            return text
        raise ValueError("Подтверждение заказа не появилось")
