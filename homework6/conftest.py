import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

from homework6.logger_obj import logging



def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="http://localhost:8081", help="Endpoint URL to test"
    )
    parser.addoption(
        "--browser", action="store", default="chrome", help="Select browser to work with"
    )
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--bversion", action="store", default="83.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    test_name = request.node.name

    logger = logging.getLogger('BrowserLogger')

    logger.info("===> Test {} started".format(test_name))

    if executor == "local":
        if browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            # default is Chrome
            driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x1024",
            "name": "OpenCart tests",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
        driver.maximize_window()

    logger.info("Browser {} started with {}".format(browser, driver.desired_capabilities))

    driver.get(url)
    logger.info("Opening {}".format(url))

    yield driver

    driver.quit()

    logger.info("===> Test {} finished".format(test_name))
