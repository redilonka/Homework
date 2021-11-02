from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework6.page_objects.BasePage import BasePage


class MainPage(BasePage):
    TIMEOUT = 10

    SEARCH =            (By.ID, "search")
    CART =              (By.ID, "cart")
    MENU =              (By.ID, "menu")
    CONTENT =           (By.ID, "content")
    COMMON_HOME =       (By.ID, "common-home")
    FOOTER =            (By.CSS_SELECTOR, "footer")
    ACCOUNT_DROPDOWN =  (By.CSS_SELECTOR, "ul.list-inline > li.dropdown")
    LOGIN_LINK =        (By.CSS_SELECTOR, "ul.list-inline > li.dropdown > ul.dropdown-menu > li:nth-child(2)")
    SHOPPING_CART =     (By.CSS_SELECTOR, "div#top-links > ul.list-inline > li > a[title='Shopping Cart']")
    DESKTOPS_DROPDOWN = (By.CSS_SELECTOR, "ul.navbar-nav > li.dropdown:nth-child(1)")
    DESKTOPS_SEE_ALL =  (By.CSS_SELECTOR, "ul.navbar-nav > li.dropdown:nth-child(1) > div.dropdown-menu > a.see-all")
    IMAC_DROPDOWN =     (By.CSS_SELECTOR, "ul.navbar-nav > li.dropdown:nth-child(1) > div.dropdown-menu > div.dropdown-inner > ul.list-unstyled > li:nth-child(2)")
    ITEM_THUMBMAIL =    (By.CSS_SELECTOR, "div.product-thumb > div.image")


    def check_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH), "Search element is not located")
        self.wait.until(EC.visibility_of_element_located(self.CART), "Cart is not located")
        self.wait.until(EC.visibility_of_element_located(self.MENU), "Footer links are absent")
        self.wait.until(EC.visibility_of_element_located(self.CONTENT), "Content block is absent")
        self.wait.until(EC.visibility_of_element_located(self.COMMON_HOME), "Common home element is absent")
        self.wait.until(EC.visibility_of_element_located(self.FOOTER), "Footer loading error")

    def check_selected_currency(self, currency):
        cart = self.wait.until(EC.visibility_of_element_located(self.CART), "Cart is not located")
        cart_total = cart.find_element_by_id("cart-total")

        assert currency in cart_total.text

    def open_login_page(self):
        self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_DROPDOWN),
            "Account dropdown is not located").click()
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK)).click()
    
    def open_cart_page(self):
        self.wait.until(EC.visibility_of_element_located(self.SHOPPING_CART), 
            "Cart element is not located").click()

    def open_desktops(self):
        self.wait.until(EC.visibility_of_element_located(self.DESKTOPS_DROPDOWN),
            "Desktop dropdown is not located").click()
        self.wait.until(EC.visibility_of_element_located(self.DESKTOPS_SEE_ALL), 
            "Desktop see all dropdown is not located").click()

    def open_imac_page(self):
        self.wait.until(EC.visibility_of_element_located(self.DESKTOPS_DROPDOWN),
            "Desktop dropdown is not located").click()
        self.wait.until(EC.visibility_of_element_located(self.IMAC_DROPDOWN),
            "Imac dropdown is not located").click()
        self.wait.until(EC.visibility_of_element_located(self.ITEM_THUMBMAIL),
            "Imac item thumbmain is not located").click()
