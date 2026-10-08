import allure
from locators import trackpage_locators as locators
from pages.base_page import BasePage


class TrackPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = locators

    @allure.step('Кликаем на логотип скутера')
    def scooter_click(self) -> None:
        self.click_element(
            self.find_element_with_scroll(self.locators.SCOO_LOGO))
