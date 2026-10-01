import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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
    @pytest.mark.parametrize("question, panel_text", questions)
    def test_question_right_text(self, driver, question, panel_text):
        home_page = HomePage(driver)
        home_page.step_search_question_and_select(question)
        assert True
