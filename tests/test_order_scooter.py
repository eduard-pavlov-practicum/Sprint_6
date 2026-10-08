import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.track_page import TrackPage
from helpers.constants import ButtonPlaces, test_data_1, test_data_2, BASE_URL, YA_URL


class TestHomePageOrderScooter:

    @allure.title('Проверка заказа самоката. ')
    @allure.description('Заказ самоката. Весь флоу позитивного сценария с двумя наборами данных.')
    @pytest.mark.parametrize("button_place, client_data", [(ButtonPlaces.BOTTOM, test_data_1), (ButtonPlaces.TOP, test_data_2)])
    def test_order_scooter_positive(self, driver, button_place, client_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.find_and_click_order_button(button_place)
        order_page.make_order(client_data)
        order_page.fill_rent_details(client_data)
        order_page.close_are_you_sure_modal()
        confirmation = order_page.get_confirmation_modal_view_text()
        assert "Заказ оформлен" in confirmation, "Ошибка создания заказа. Нет подтверждения."

        tracking_page = TrackPage(driver)

        tracking_page.scooter_click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL, "Главная страница не открылась"

        scooter_tab = driver.current_window_handle
        home_page.ya_click()
        WebDriverWait(driver, 10).until(
            expected_conditions.number_of_windows_to_be(2))

        new_tab = [h for h in driver.window_handles if h != scooter_tab][0]

        driver.switch_to.window(new_tab)

        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(YA_URL))
        assert driver.current_url == YA_URL, "Сайт Яндекса не открылся"
