import requests


def get_result(endpoint, status):
    """
    Get result from API and assert for status.
    """
    result = requests.get(endpoint)

    assert result.status_code == status

    return result
