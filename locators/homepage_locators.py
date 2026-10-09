from selenium.webdriver.common.by import By

from helpers.constants import ButtonPlaces

COOKIE_BUTTON = (By.XPATH, '//button[starts-with(@class,"App_CookieButton")]')
IMPORTANT_QUESTIONS_HEADING = (By.XPATH, '//div[text()="Вопросы о важном"]')
IMPORTANT_QUESTIONS_ITEMS = (By.XPATH, IMPORTANT_QUESTIONS_HEADING[1] +
                             '/following-sibling::div[starts-with(@class, "Home_FAQ")]//div[@data-accordion-component="AccordionItemHeading"]')
IMPORTANT_QUESTIONS_BUTTON = (
    By.XPATH, './/div[@data-accordion-component="AccordionItemButton"]')
IMPORTANT_QUESTIONS_PANEL = (
    By.XPATH, './following-sibling::div[@data-accordion-component="AccordionItemPanel"]')

ORDER_BUTTONS = {ButtonPlaces.BOTTOM: (By.XPATH, '//div[starts-with(@class,"Home_FinishButton")]//button[text()="Заказать"]'),
                 ButtonPlaces.TOP: (By.XPATH, '//div[starts-with(@class,"Header")]//button[text()="Заказать"]')}

YA_LOGO = (By.XPATH, '//a[starts-with(@class,"Header_LogoYandex")]')
