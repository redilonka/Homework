import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="Endpoint URL to test"
    )
    parser.addoption(
        "--status_code", action="store", default="200", help="Status code to check"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    # We don't use additional check for int base here yet
    return int(request.config.getoption("--status_code"))
