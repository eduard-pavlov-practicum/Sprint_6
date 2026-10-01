import allure
from locators import homepage_locators as lc
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def find_questions_block(self):
        element = self.driver.find_element(*lc.IMPORTANT_QUESTIONS_HEADING)
        self.scroll_to_element(element)
        return element

    def find_questions(self):
        return self.driver.find_elements(*lc.IMPORTANT_QUESTIONS_ITEMS)

    def find_button(self, question_item):
        button = question_item.find_element(*lc.IMPORTANT_QUESTIONS_BUTTON)
        self.scroll_to_element(button)
        return button

    def question_button_click(self, button):
        self.wait_element_clickable(button)
        button.click()

    def get_question_panel_text(self, question_item):
        return question_item.find_element(*lc.IMPORTANT_QUESTIONS_PANEL).text

    # def step_find_question(self, etalon_question):
    #     questions_items = self.find_questions_block()
    #     question = [item for item in questions_items if self.get_question_text(
    #         item) == etalon_question]

    @allure.step('Ищем вопрос "{}" и выбираем его')
    def step_search_question_and_select(self, question):
        self.find_questions_block
        question_items = self.find_questions()
        for item in question_items:
            button = self.find_button(item)
            if button.text == question:
                self.question_button_click(button)
