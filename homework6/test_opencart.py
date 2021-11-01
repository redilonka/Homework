from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, url):
    """Open main opencart page"""
    browser.get(url)

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.ID, "search")), "Search element is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "cart")), "Cart is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "menu")), "Footer links are absent")
    wait.until(EC.visibility_of_element_located((By.ID, "content")), "Content block is absent")
    wait.until(EC.visibility_of_element_located((By.ID, "common-home")), "Common home element is absent")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")), "Footer loading error")


def test_desktops_page(browser, url):
    """Open desktops opencart page"""
    browser.get(urljoin(url, "/desktops"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")), "Breadcrumb loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group")), "List group loading error")
    wait.until(EC.visibility_of_element_located((By.ID, "content")), "Content loading error")
    wait.until(EC.visibility_of_element_located((By.ID, "compare-total")), "Compare element loading error")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")), "Footer loading error")


def test_login_page(browser, url):
    """Open login opencart page"""
    browser.get(urljoin(url, "/index.php?route=account/login"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.ID, "search")), "Search element is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "cart")), "Cart is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "menu")), "Footer links are absent")
    wait.until(EC.visibility_of_element_located((By.ID, "content")), "Content block is absent")
    wait.until(EC.visibility_of_element_located((By.ID, "account-login")), "Account login holder loading error")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")), "Footer loading error")


def test_cart_page(browser, url):
    """Open cart page"""
    browser.get(urljoin(url, "/index.php?route=checkout/cart"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.ID, "search")), "Search element is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "cart")), "Cart is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "menu")), "Footer links are absent")
    wait.until(EC.visibility_of_element_located((By.ID, "content")), "Content block is absent")
    el = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > p")), "Shoring cart empty message not found")
    assert el.text == "Your shopping cart is empty!"


def test_item_page(browser, url):
    """Open particular item"""
    browser.get(urljoin(url, "/desktops/mac/imac"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.ID, "search")), "Search element is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "cart")), "Cart is not located")
    wait.until(EC.visibility_of_element_located((By.ID, "menu")), "Footer links are absent")
    wait.until(EC.visibility_of_element_located((By.ID, "content")), "Content block is absent")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content .thumbnails")), "Thumbnails block is absent")
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")), "Add to wish list element is absent")
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")), "Compate this Product element is absent")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")), "Footer loading error")


def test_admin_page(browser, url):
    """Open admin page"""
    browser.get(urljoin(url, "/admin"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "panel-default")), "Panel main element loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "help-block")), "Help block loading error")
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")), "Input username element loading error")
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")), "Input password element loading error")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")), "Login form submit loading error")
