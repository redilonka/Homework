from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework6.page_objects.BasePage import BasePage
from homework6.elements.NewUserForm import NewUserForm


class AdminPage(BasePage):
    TIMEOUT = 10

    PANEL_DEFAULT =            (By.CLASS_NAME, "panel-default")
    HELP_BLOCK =               (By.CLASS_NAME, "help-block")
    USERNAME =                 (By.ID, "input-username")
    PASSWORD =                 (By.ID, "input-password")
    SUBMIT =                   (By.CSS_SELECTOR, "button[type='submit']")

    MENU_CATALOG =             (By.ID, "menu-catalog")
    PRODUCTS =                 (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_NEW =                  (By.CSS_SELECTOR, ".pull-right > a[data-original-title='Add New']")
    PRODUCT_DESCRIPTION_NAME = (By.CSS_SELECTOR, "input[name='product_description[1][name]']")
    PRODUCT_DESCRIPTION_META = (By.CSS_SELECTOR, "input[name='product_description[1][meta_title]']")
    PRODUCT_DATA =             (By.CSS_SELECTOR, "ul > li > a[href='#tab-data']")
    PRODUCT_MODEL =            (By.CSS_SELECTOR, "input#input-model")
    SAVE_BTN =                 (By.CSS_SELECTOR, "button[type='submit'][data-original-title='Save']")

    FILTER_BY_NAME =           (By.ID, "input-name")
    BTN_FILTER =               (By.ID, "button-filter")
    SELECT_ALL_CHECKBOX =      (By.CSS_SELECTOR, "thead > tr > td:nth-child(1)")
    DELETE_BTN =               (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    SUCCESS_MSG =              (By.CSS_SELECTOR, "div.alert-success")

    MENU_SYSTEM =              (By.ID, "menu-system")
    MENU_USERS =               (By.CSS_SELECTOR, "#menu-system  li:nth-child(2)")
    SUBMENU_USERS =            (By.CSS_SELECTOR, "#menu-system  li:nth-child(2) li:nth-child(1)")

    USER_CHECKBOX =            (By.XPATH, "//table/tbody//td[contains(text(), '{}')]")

    def check_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.PANEL_DEFAULT), "Panel main element loading error")
        self.wait.until(EC.visibility_of_element_located(self.HELP_BLOCK), "Help block loading error")
        self.wait.until(EC.visibility_of_element_located(self.USERNAME), "Input username element loading error")
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD), "Input password element loading error")
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT), "Login form submit loading error")

    def login(self, username, password):
        username_input = self.wait.until(EC.visibility_of_element_located(self.USERNAME), "Input username element loading error")
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD), "Input password element loading error")
        submit = self.wait.until(EC.visibility_of_element_located(self.SUBMIT), "Login form submit loading error")

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit.click()

    def open_products_page(self):
        self.wait.until(EC.visibility_of_element_located(self.MENU_CATALOG), "Menu catalog loading error").click()
        self.wait.until(EC.visibility_of_element_located(self.PRODUCTS), "Products menu can't be find").click()

    def add_new_product(self, name="Test name", meta_tag="Test meta", model="Test model"):
        self.wait.until(EC.visibility_of_element_located(self.ADD_NEW), "Can't locate Add New button").click()
        self.wait.until(EC.visibility_of_element_located(
            self.PRODUCT_DESCRIPTION_NAME), "Can't locate product description").send_keys(name)
        self.wait.until(EC.visibility_of_element_located(
            self.PRODUCT_DESCRIPTION_META), "Can't locate product meta").send_keys(meta_tag)
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_DATA), "Can't locate product data tab").click()
        self.wait.until(EC.visibility_of_element_located(
            self.PRODUCT_MODEL), "Can't locate product model").send_keys(model)
        
        self.wait.until(EC.visibility_of_element_located(self.SAVE_BTN), "Can't locate Save button").click()

    def delete_product(self, name="Test name"):
        self.wait.until(EC.visibility_of_element_located(
            self.FILTER_BY_NAME), "Can't locate product name filter input").send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.BTN_FILTER), "Can't locate button filter").click()
        self.wait.until(EC.visibility_of_element_located(self.SELECT_ALL_CHECKBOX), "Can't locate product checkbox").click()
        self.wait.until(EC.visibility_of_element_located(self.DELETE_BTN), "Can't locate delete button").click()

        self.browser.switch_to.alert.accept()

        success_msg = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG), "Can't locate product success edit msg")

        assert "Success" in success_msg.text

    def open_menu_users(self):
        self.wait.until(EC.visibility_of_element_located(self.MENU_SYSTEM), "Can't locate button filter").click()
        self.wait.until(EC.visibility_of_element_located(self.MENU_USERS), "Can't open Users menu").click()
        self.wait.until(EC.visibility_of_element_located(self.SUBMENU_USERS), "Can't open Useers sub-menu").click()

    def add_new_user(self, username, password, email, first_name, last_name):
        self.wait.until(EC.visibility_of_element_located(self.ADD_NEW), "Can't locate Add New button").click()

        new_user_form = NewUserForm(self.browser)
        new_user_form.fill(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name).activate()

        self.wait.until(EC.visibility_of_element_located(self.SAVE_BTN), "Can't locate Save button").click()

    def delete_user(self, username):
        # Inject username into XPATH
        USER_CHECKBOX = self.USER_CHECKBOX[0], self.USER_CHECKBOX[1].format(username)

        self.wait.until(
            EC.visibility_of_element_located(USER_CHECKBOX),
            "Can't locate user item").find_element_by_xpath("../td").click()

        sleep(1)  # Can't handle :after for checkbox properly
        self.wait.until(EC.visibility_of_element_located(self.DELETE_BTN), "Can't locate delete button").click()
        sleep(1)  # Have to wait some time for alert - don't understand why yet
        self.browser.switch_to.alert.accept()
