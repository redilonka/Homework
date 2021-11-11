import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework6.page_objects.BasePage import BasePage


class ItemPage(BasePage):
    TIMEOUT = 10

    SEARCH =          (By.ID, "search")
    CART =            (By.ID, "cart")
    MENU =            (By.ID, "menu")
    CONTENT =         (By.ID, "content")
    THUMBNAILS =      (By.CSS_SELECTOR, "#content .thumbnails")
    WISH_LIST =       (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    FOOTER =          (By.CSS_SELECTOR, "footer")

    @allure.step
    def check_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH), "Search element is not located")
        self.wait.until(EC.visibility_of_element_located(self.CART), "Cart is not located")
        self.wait.until(EC.visibility_of_element_located(self.MENU), "Footer links are absent")
        self.wait.until(EC.visibility_of_element_located(self.CONTENT), "Content block is absent")
        self.wait.until(EC.visibility_of_element_located(self.THUMBNAILS), "Thumbnails block is absent")
        self.wait.until(EC.visibility_of_element_located(self.WISH_LIST), "Add to wish list element is absent")
        self.wait.until(EC.visibility_of_element_located(self.COMPARE_PRODUCT), "Compate this Product element is absent")
        self.wait.until(EC.visibility_of_element_located(self.FOOTER), "Footer loading error")
