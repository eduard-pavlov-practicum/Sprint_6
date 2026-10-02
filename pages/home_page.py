import allure
from selenium.webdriver.remote.webelement import WebElement
from locators import homepage_locators as locators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = locators

    def find_questions_block(self):
        element = self.driver.find_element(
            *self.locators.IMPORTANT_QUESTIONS_HEADING)
        self.scroll_to_element(element)
        return element

    def find_questions(self):
        return self.driver.find_elements(*self.locators.IMPORTANT_QUESTIONS_ITEMS)

    def find_button(self, question_item):
        button = question_item.find_element(
            *self.locators.IMPORTANT_QUESTIONS_BUTTON)
        self.scroll_to_element(button)
        return button

    def question_button_click(self, button):
        self.wait_element_clickable(button)
        button.click()

    @allure.step('Ищем панель с ответом')
    def get_question_panel(self, question_item) -> WebElement:
        return question_item.find_element(*self.locators.IMPORTANT_QUESTIONS_PANEL)

    @allure.step('Ищем вопрос "{}" и выбираем его')
    def step_search_question_and_select(self, question) -> WebElement | None:
        self.find_questions_block
        question_items = self.find_questions()
        for item in question_items:
            button = self.find_button(item)
            if button.text == question:
                self.question_button_click(button)
                return item
        return None
