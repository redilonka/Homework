import requests


def test_endpoint(url, status_code):
    assert requests.get(url).status_code == status_code
