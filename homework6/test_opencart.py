from urllib.parse import urljoin

from homework6.page_objects.MainPage import MainPage
from homework6.page_objects.DesktopsPage import DesktopsPage
from homework6.page_objects.LoginPage import LoginPage
from homework6.page_objects.CartPage import CartPage
from homework6.page_objects.ItemPage import ItemPage
from homework6.page_objects.AdminPage import AdminPage
from homework6.elements.CurrencySelector import CurrencySelector


def test_main_page(browser):
    """Open main opencart page"""
    MainPage(browser).check_elements()


def test_desktops_page(browser, url):
    """Open desktops opencart page"""
    MainPage(browser).open_desktops()
    DesktopsPage(browser).check_elements()


def test_login_page(browser, url):
    """Open login opencart page"""
    MainPage(browser).open_login_page()
    LoginPage(browser).check_elements()


def test_cart_page(browser):
    """Open cart page"""
    MainPage(browser).open_cart_page()
    CartPage(browser).check_elements()


def test_item_page(browser, url):
    """Open particular item"""
    MainPage(browser).open_imac_page()
    ItemPage(browser).check_elements()


def test_change_currency(browser):
    main_page = MainPage(browser)

    currency_selector = CurrencySelector(browser)
    currency_selector.open()
    currency_selector.select(CurrencySelector.EUR)

    main_page.check_selected_currency(CurrencySelector.EUR_SIGN)


def test_admin_page(browser, url):
    """Open admin page"""
    browser.get(urljoin(url, "/admin"))

    AdminPage(browser).check_elements()


def test_add_product(browser, url):
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")
    admin_page.open_products_page()
    admin_page.add_new_product("Test name", "Test meta", "Test model")


def test_delete_product(browser, url):
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")
    admin_page.open_products_page()
    admin_page.delete_product("Test name")


def test_add_user(browser, url):
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


def test_delete_user(browser, url):
    browser.get(urljoin(url, "/admin"))

    admin_page = AdminPage(browser)
    admin_page.login("user", "1234")

    admin_page.open_menu_users()
    admin_page.delete_user(username="new_user")
