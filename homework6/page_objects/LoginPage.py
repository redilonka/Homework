from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework6.page_objects.BasePage import BasePage


class LoginPage(BasePage):
    TIMEOUT = 10

    SEARCH =        (By.ID, "search")
    CART =          (By.ID, "cart")
    MENU =          (By.ID, "menu")
    CONTENT =       (By.ID, "content")
    ACCOUNT_LOGIN = (By.ID, "account-login")
    FOOTER =        (By.CSS_SELECTOR, "footer")

    def check_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH), "Search element is not located")
        self.wait.until(EC.visibility_of_element_located(self.CART), "Cart is not located")
        self.wait.until(EC.visibility_of_element_located(self.MENU), "Footer links are absent")
        self.wait.until(EC.visibility_of_element_located(self.CONTENT), "Content block is absent")
        self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_LOGIN), "Account login holder loading error")
        self.wait.until(EC.visibility_of_element_located(self.FOOTER), "Footer loading error")
