from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, url):
    """Open main opencart page"""
    browser.get(url)

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    el = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".download-content-inner > .download-content-abs a#button-demo")),
        "Online demoo element is not presented")
    assert el.text == "ОНЛАЙН-ДЕМО"

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart__grup")), "Cart group is not located")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-links")), "Footer links are absent")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-header")), "Navbar is absent")
    wait.until(EC.visibility_of_element_located((By.ID, "cart-total-img")), "Cart total image is absent")


def test_blog_page(browser, url):
    """Open blog opencart page"""
    browser.get(urljoin(url, "/blog"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")), "Breadcrumb loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "grid__list")), "Grid list loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "grid__table")), "Grid table loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "blog_grid_holder")), "Blog grid holder loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "main__pagination")), "Paginaton loading error")


def test_documentation_page(browser, url):
    """Open documentation opencart page"""
    browser.get(urljoin(url, "/documentation"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")), "Breadcrumb loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "blog__page-title")), "Blog page title loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-header")), "Navbar is absent")
    wait.until(EC.visibility_of_element_located((By.ID, "menu_category")), "Menu category loading error")
    wait.until(EC.visibility_of_element_located((By.ID, "content")), "Content element loading error")


def test_modules_page(browser, url):
    """Open modules opencart page"""
    browser.get(urljoin(url, "/modules"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")), "Breadcrumb loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "blog__page-title")), "Blog page title loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group")), "List group loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category__sort")), "Sorting loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category__search")), "Search element loading error")


def test_item_page(browser, url):
    """
    Open particular item.
    
    Note:
    - it's hardcoded for now
    - can disappear
    - if it critical I can select an item to test dynamically
      from modules page
    """
    browser.get(urljoin(url, "/amigration-perenos-dannyh-s-opencart-15-na-opencart-2-modul-migracii-osnovnyh-dannyh-301"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")), "Breadcrumb loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "blog__page-title")), "Blog page title loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group")), "List group loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product__item")), "Product row loading error")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product__page")), "Product page loading error")


def test_admin_page(browser, url):
    """Open admin page"""
    browser.get(urljoin(url, "/admin"))

    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")), "Breadcrumb loading error")
    el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "blog__page-title")),
        "Blog page title loading error")
    assert el.text == "Запрашиваемая страница не найдена!"
