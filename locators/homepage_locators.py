from selenium.webdriver.common.by import By


IMPORTANT_QUESTIONS_HEADING = (By.XPATH, '//div[text()="Вопросы о важном"]')
IMPORTANT_QUESTIONS_ITEMS = (By.XPATH, IMPORTANT_QUESTIONS_HEADING[1] +
                             '/following-sibling::div[starts-with(@class, "Home_FAQ")]//div[@data-accordion-component="AccordionItemHeading"]')
IMPORTANT_QUESTIONS_BUTTON = (
    By.XPATH, './/div[@data-accordion-component="AccordionItemButton"]')
IMPORTANT_QUESTIONS_PANEL = (
    By.XPATH, './following-sibling::div[@data-accordion-component="AccordionItemPanel"]')
