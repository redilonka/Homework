"""
Contracts testing for placeholder.
"""
from urllib.parse import urljoin

import pytest


from homework5.placeholder.utils import get_result


def test_base(base_url):
    """
    Testing base endpoint.
    """
    endpoint = urljoin(base_url, "/posts")
    result = get_result(endpoint=endpoint, status=200)

    assert type(result.json()) == list

    obj = result.json()[0]
    assert type(obj) == dict

    for key in ("userId", "id", "title", "body"):
        assert key in obj


@pytest.mark.parametrize("id", [1, 3, 15, 50, 51])
def test_posts_multiple(base_url, id):
    """
    Testing lists of posts.
    """
    endpoint = urljoin(base_url, f"/posts/{id}")
    result = get_result(endpoint=endpoint, status=200)

    assert "title" in result.json()


@pytest.mark.parametrize("postId", [1, 100])
def test_comments_for_post(base_url, postId):
    """
    Testing comments for one posts.
    """
    endpoint = urljoin(base_url, f"/comments/?postId={postId}")
    result = get_result(endpoint=endpoint, status=200)

    for comment in result.json():
        assert "email" in comment


def test_base_users(base_url):
    """
    Testing base endpoint.
    """
    endpoint = urljoin(base_url, "/users")
    result = get_result(endpoint=endpoint, status=200)

    assert type(result.json()) == list

    obj = result.json()[0]
    assert type(obj) == dict

    for key in ("id", "name", "username", "email", "address"):
        assert key in obj


def test_base_todos(base_url):
    """
    Testing base endpoint to-do.
    """
    endpoint = urljoin(base_url, "/todos")
    result = get_result(endpoint=endpoint, status=200)

    assert type(result.json()) == list

    obj = result.json()[0]
    assert type(obj) == dict

    for key in ("id", "userId", "title", "completed"):
        assert key in obj