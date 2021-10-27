"""
Contracts testing for brewery.
"""
from urllib.parse import urljoin

import pytest

from homework5.brewery.utils import get_result


def test_base(base_url):
    """
    Testing base endpoint.
    """
    endpoint = base_url
    result = get_result(endpoint=endpoint, status=200)

    obj = result.json()[0]

    for key in ("id", "name", "brewery_type"):
        assert key in obj


@pytest.mark.parametrize("city", ["san_diego", "new_york", "alameda"])
def test_filter_by_city(base_url, city):
    """
    Testing location for search.
    """
    _maping = {
        "san_diego": "San Diego",
        "new_york": "New York",
        "alameda": "Alameda",
    }

    endpoint = urljoin(base_url, f"?by_city={city}")
    result = get_result(endpoint=endpoint, status=200)

    for breweries in result.json():
        assert "city" in breweries
        assert breweries["city"] == _maping[city]


@pytest.mark.parametrize("query", ["dog", "brew",])
def test_search_by_autocomplete(base_url, query):
    """
    Testing search by query.
    """

    endpoint = urljoin(base_url, f"autocomplete/?query={query}")
    result = get_result(endpoint=endpoint, status=200)

    for search_result in result.json():
        assert query in search_result["name"].lower()
       

    
@pytest.mark.parametrize("id", [12432, 3])
def test_search_by_id_wrong_id_format(base_url, id):
    """
    Testing search by id
    """
    error_msg = "Couldn't find Brewery"
    endpoint = urljoin(base_url, f"{id}")
    result = get_result(endpoint=endpoint, status=404)

    assert type(result.json()) == dict
    assert result.json()["message"] == error_msg


@pytest.mark.parametrize("id", ["bnaf-llc-austin", "epidemic-ales-concord"])
def test_search_by_id(base_url, id):
    """
    Testing search by id
    """
    keys =  (
        "id",
        "name",
        "brewery_type",
        "street",
        "address_2",
        "address_3",
        "city",
        "state",
        "county_province",
        "postal_code",
        "country",
        "longitude",
        "latitude",
        "phone",
        "website_url",
        "updated_at",
        "created_at",
    )
    endpoint = urljoin(base_url, f"{id}")
    result = get_result(endpoint=endpoint, status=200)

    assert type(result.json()) == dict
    assert result.json()["id"] == id

    for key in keys:
        assert key in result.json()