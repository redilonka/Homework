import allure
from selenium.webdriver.common.by import By

from homework6.page_objects.BasePage import BasePage
from homework6.logger_obj import logging

log = logging.getLogger("CurreencySelector")


class CurrencySelector(BasePage):
    EUR = "EUR"
    EUR_SIGN = "€"

    GBP = "GBP"
    GBP_SIGN = "£"

    USD = "USD"
    USD_SIGN = "$"

    CURRENCY_SELECTOR = (By.CSS_SELECTOR, "form#form-currency")

    @allure.step
    def open(self):
        self._element(self.CURRENCY_SELECTOR).click()
        log.info("Open currency selector dropdown")

    @allure.step
    def select(self, value):
        self._element(self.CURRENCY_SELECTOR).find_element_by_name(value).click()
        log.info(f"Changing currency to {value}")
