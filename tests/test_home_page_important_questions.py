import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from pages.home_page import HomePage
from locators import homepage_locators as lc


class TestHomePageImportantQuestions:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном». ')
    @allure.description('На странице ищем вопрос и проверяем, после его выбора появляется ожидаемый ответ')
    @pytest.mark.parametrize("question, expected_answer", questions)
    def test_question_right_text(self, driver, question, expected_answer):
        home_page = HomePage(driver)
        active_question_accordion_item = home_page.step_search_question_and_select(
            question)
        assert active_question_accordion_item is not None, f"Вопрос \"{question[0:10]+'...'}\" не найден"
        answer_panel = home_page.get_question_panel(
            active_question_accordion_item)
        assert answer_panel.get_attribute(
            'hidden') is None, f'Ответ на вопрос \"{question[0:10]+'...'}\" скрыт'
        answer = answer_panel.text
        assert answer == expected_answer, f'Ответ на вопрос не соответсвует ожидаемому. Ожидался "{expected_answer}", получен "{answer}"'
