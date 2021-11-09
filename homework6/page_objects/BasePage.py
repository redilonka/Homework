from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 10

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, self.TIMEOUT, poll_frequency=1)

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.TIMEOUT).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)
