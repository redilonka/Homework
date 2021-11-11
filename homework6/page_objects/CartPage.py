import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework6.page_objects.BasePage import BasePage


class CartPage(BasePage):
    TIMEOUT = 10

    SEARCH =         (By.ID, "search")
    CART =           (By.ID, "cart")
    MENU =           (By.ID, "menu")
    CONTENT =        (By.ID, "content")
    CART_EMPTY_SMG = (By.CSS_SELECTOR, "#content > p")

    @allure.step
    def check_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH), "Search element is not located")
        self.wait.until(EC.visibility_of_element_located(self.CART), "Cart is not located")
        self.wait.until(EC.visibility_of_element_located(self.MENU), "Footer links are absent")
        self.wait.until(EC.visibility_of_element_located(self.CONTENT), "Content block is absent")

        el = self.wait.until(EC.visibility_of_element_located(self.CART_EMPTY_SMG), "Shopping cart empty message not found")
        assert el.text == "Your shopping cart is empty!"
