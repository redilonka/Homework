from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from homework6.page_objects.BasePage import BasePage


class NewUserForm(BasePage):
    USERNAME = (By.CSS_SELECTOR, "input[type='text'][name='username']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[type='text'][name='firstname']")
    LAST_NAME = (By.CSS_SELECTOR, "input[type='text'][name='lastname']")
    EMAIL = (By.CSS_SELECTOR, "input[type='text'][name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password'][name='password']")
    CONFIRM = (By.CSS_SELECTOR, "input[type='password'][name='confirm']")
    STATUSES = (By.ID, "input-status")

    def fill(self, username, password, email, first_name, last_name):
        self._element(self.USERNAME).send_keys(username)
        self._element(self.FIRST_NAME).send_keys(first_name)
        self._element(self.LAST_NAME).send_keys(last_name)
        self._element(self.EMAIL).send_keys(email)
        self._element(self.PASSWORD).send_keys(password)
        self._element(self.CONFIRM).send_keys(password)

        return self

    def activate(self):
        select = Select(self._element(self.STATUSES))
        select.select_by_value("1")

    def deactivate(self):
        select = Select(self._element(self.STATUSES))
        select.select_by_value("0")
