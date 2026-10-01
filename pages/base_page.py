from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def scroll_to_element(self, element: WebElement):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)
        self.wait_element_visible(element)

    def wait_element_visible(self, element: WebElement):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of(element))

    def wait_element_clickable(self, element: WebElement):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(element))
