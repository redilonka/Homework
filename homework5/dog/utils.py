import requests


def get_result(endpoint, status, status_str):
    """
    Get result from API and assert for status.
    """
    result = requests.get(endpoint)

    assert result.status_code == status

    assert "message" in result.json().keys()
    assert "status"  in result.json().keys()

    assert result.json()["status"] == status_str

    return result
