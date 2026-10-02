import pytest
import allure
from pages.home_page import HomePage


class TestHomePageImportantQuestions:
    questions = [
        ('Сколько это стоит? И как оплатить?',
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        ('Хочу сразу несколько самокатов! Так можно?',
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        ('Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    ]

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
