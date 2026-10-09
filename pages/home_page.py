import allure
from selenium.webdriver.remote.webelement import WebElement
from locators import homepage_locators as locators
from pages.base_page import BasePage
from helpers.constants import ButtonPlaces


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = locators

    def find_questions_block(self):
        return self.find_element_with_scroll(self.locators.IMPORTANT_QUESTIONS_HEADING)

    def find_questions(self):
        return self.driver.find_elements(*self.locators.IMPORTANT_QUESTIONS_ITEMS)

    def find_question_button(self, question_item: WebElement):
        return self.find_element_in_block(question_item, self.locators.IMPORTANT_QUESTIONS_BUTTON)

    def question_button_click(self, button: WebElement):
        self.click_element(button)

    @allure.step("Убираем плашку с предупреждением про куки")
    def hide_cookie_warning(self):
        self.click_element(self.find_element_with_scroll(
            self.locators.COOKIE_BUTTON))

    @allure.step('Ищем панель с ответом')
    def get_question_panel(self, question_item: WebElement) -> WebElement:
        return self.wait_element_visible(self.find_element_in_block(
            question_item, self.locators.IMPORTANT_QUESTIONS_PANEL))

    @allure.step('Ищем вопрос "{question_text}" и получаем текст ответа')
    def get_answer_for_question(self, question_text: str) -> str:
        self.hide_cookie_warning()
        self.find_questions_block()
        questions = self.find_questions()

        for item in questions:
            button = self.find_question_button(item)
            if button.text == question_text:
                self.question_button_click(button)

                panel = self.get_question_panel(item)
                return panel.text

        raise ValueError(f"Вопрос с текстом '{question_text}' не найден")

    @allure.step('Ищем и нажимаем кнопку "Заказать" в положении {button_place}')
    def find_and_click_order_button(self, button_place: ButtonPlaces):
        self.hide_cookie_warning()
        button = self.wait_element_clickable(self.find_element_with_scroll(
            self.locators.ORDER_BUTTONS[button_place]))
        button.click()

        return button

    @allure.step('Кликаем на логотип Яндекса')
    def ya_click(self) -> None:
        self.click_element(
            self.find_element_with_scroll(self.locators.YA_LOGO))
