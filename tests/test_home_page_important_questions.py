import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from pages.home_page import HomePage
from locators import homepage_locators as lc


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

        answer = home_page.get_answer_for_question(
            question_text=question)
        assert answer == expected_answer, f'Ответ на вопрос не соответсвует ожидаемому. Ожидался "{expected_answer}", получен "{answer}"'
