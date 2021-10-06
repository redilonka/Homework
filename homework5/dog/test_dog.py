"""
Contracts testing for dogs.
"""
from urllib.parse import urljoin
from random import choice

import pytest
import requests

from homework5.dog.utils import get_result


def test_list_all(base_url):
    """
    Testing list all sub-endpoint.
    """
    endpoint = urljoin(base_url, "breeds/list/all")
    result = get_result(endpoint=endpoint, status=200, status_str="success")

    assert type(result.json()["message"]) == dict
    assert type(result.json()["message"]["poodle"]) == list


def test_image_random(base_url):
    """
    Testing image random sub-endpoint.
    """
    endpoint = urljoin(base_url, "breeds/image/random")
    result = get_result(endpoint=endpoint, status=200, status_str="success")

    assert type(result.json()["message"]) == str

    image_url = result.json()["message"]
    assert image_url.split(".")[-1] in ("jpg", "jpeg")

    assert requests.get(image_url).status_code == 200


@pytest.mark.parametrize("count", [0, 3, 15, 50, 51, -1])
def test_image_random_multiple(base_url, count):
    """
    Testing image random sub-endpoint.
    """
    _maping = {
        -1: 1,
        0:  1,
        51: 50,
    }

    endpoint = urljoin(base_url, f"breeds/image/random/{count}")
    result = get_result(endpoint=endpoint, status=200, status_str="success")

    assert type(result.json()["message"]) == list

    # API acts very strange
    # 51 returns 50 items and it's OK
    # 0 returns 1 item and it's strange :)
    assert len(result.json()["message"]) == _maping[count] if count in (-1, 0, 51) else count

    random_img = choice(result.json()["message"])

    assert requests.get(random_img).status_code == 200


@pytest.mark.parametrize("breed", ["hound", "mastiff"])
def test_by_breed(base_url, breed):
    """
    Testing by breed sub-endpoint.
    """
    endpoint = urljoin(base_url, f"breed/{breed}/images")
    result = get_result(endpoint=endpoint, status=200, status_str="success")

    assert type(result.json()["message"]) == list

    random_img = choice(result.json()["message"])

    assert requests.get(random_img).status_code == 200


@pytest.mark.parametrize("breed", ["hound", "mastiff"])
def test_by_sub_breed(base_url, breed):
    """
    Testing by sub breed sub-endpoint.
    """
    endpoint = urljoin(base_url, f"breed/{breed}/list")
    result = get_result(endpoint=endpoint, status=200, status_str="success")

    assert type(result.json()["message"]) == list

    random_sub_breed = choice(result.json()["message"])

    assert isinstance(random_sub_breed, str)
