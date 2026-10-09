import pytest
import allure
from pages.home_page import HomePage
from helpers.constants import QUESTIONS


class TestHomePageImportantQuestions:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном». ')
    @allure.description('На странице ищем вопрос и проверяем, после его выбора появляется ожидаемый ответ')
    @pytest.mark.parametrize("question, expected_answer", QUESTIONS)
    def test_question_right_text(self, driver, question, expected_answer):
        home_page = HomePage(driver)

        answer = home_page.get_answer_for_question(
            question_text=question)
        assert answer == expected_answer, f'Ответ на вопрос не соответсвует ожидаемому. Ожидался "{expected_answer}", получен "{answer}"'
