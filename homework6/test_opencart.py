from urllib.parse import urljoin

import allure

from homework6.page_objects.MainPage import MainPage
from homework6.page_objects.DesktopsPage import DesktopsPage
from homework6.page_objects.LoginPage import LoginPage
from homework6.page_objects.CartPage import CartPage
from homework6.page_objects.ItemPage import ItemPage
from homework6.page_objects.AdminPage import AdminPage
from homework6.elements.CurrencySelector import CurrencySelector


@allure.title("Main page test")
@allure.description("Checking major elements on main page")
@allure.severity(allure.severity_level.NORMAL)
def test_main_page(browser):
    """Open main opencart page"""
    MainPage(browser).check_elements()


@allure.severity(allure.severity_level.MINOR)
def test_desktops_page(browser):
    """Open desktops opencart page"""
    MainPage(browser).open_desktops()
    DesktopsPage(browser).check_elements()


@allure.severity(allure.severity_level.NORMAL)
def test_login_page(browser):
    """Open login opencart page"""
    MainPage(browser).open_login_page()
    LoginPage(browser).check_elements()


@allure.severity(allure.severity_level.CRITICAL)
def test_cart_page(browser):
    """Open cart page"""
    MainPage(browser).open_cart_page()
    CartPage(browser).check_elements()


@allure.severity(allure.severity_level.NORMAL)
def test_item_page(browser, url):
    """Open particular item"""
    MainPage(browser).open_imac_page()
    ItemPage(browser).check_elements()


@allure.severity(allure.severity_level.CRITICAL)
def test_change_currency(browser):
    """Change curerncy to EUR"""
    main_page = MainPage(browser)

    currency_selector = CurrencySelector(browser)
    currency_selector.open()
    currency_selector.select(CurrencySelector.EUR)

    main_page.check_selected_currency(CurrencySelector.EUR_SIGN)


@allure.severity(allure.severity_level.MINOR)
def test_admin_page(browser, url):
    """Open admin page"""
    browser.get(urljoin(url, "/admin"))

    AdminPage(browser).check_elements()


@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Add new product")
def test_add_product(browser, url):
    """Adding new product"""
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")
    admin_page.open_products_page()
    admin_page.add_new_product("Test name", "Test meta", "Test model")


@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Delete product")
def test_delete_product(browser, url):
    """Deleting new product"""
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")
    admin_page.open_products_page()
    admin_page.delete_product("Test name")


@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Adding new User")
def test_add_user(browser, url):
    """Add User"""
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")

    admin_page.open_menu_users()
    admin_page.add_new_user(
        username="new_user",
        password="1234",
        email="new_user@email.com",
        first_name="New User first",
        last_name="New User last")


@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Deleting user by username")
def test_delete_user(browser, url):
    """Delete User"""
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")

    admin_page.open_menu_users()
    admin_page.delete_user(username="new_user")
