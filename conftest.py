import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.constants import BASE_URL


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия браузера.
    """
    driver = init_driver()
    open_page(driver, BASE_URL)

    yield driver

    quit_driver(driver)


@allure.step('Открываем браузер Firefox')  # декоратор
def init_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver


@allure.step('Открываем страницу {page}')  # декоратор
def open_page(driver, page):
    driver.get(page)


@allure.step('Закрываем браузер')  # декоратор
def quit_driver(driver):
    driver.quit()
