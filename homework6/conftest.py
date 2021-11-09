import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager



def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="http://localhost:8081", help="Endpoint URL to test"
    )
    parser.addoption(
        "--browser", action="store", default="chrome", help="Select browser to work with"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        # default is Chrome
        driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get(url)

    yield driver

    driver.quit()
