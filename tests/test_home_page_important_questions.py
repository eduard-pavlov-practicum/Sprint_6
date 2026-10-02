import pytest
import allure
from pages.home_page import HomePage


class TestHomePageImportantQuestions:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном». ')
    @allure.description('На странице ищем вопрос и проверяем, после его выбора появляется ожидаемый ответ')
    @pytest.mark.parametrize("", [])
    def test_order_scooter(self, driver, , ):
        home_page = HomePage(driver)
