import pytest

from src.Triangle import Triangle


def test_triangle_init_positive(triangle_valid):
    assert triangle_valid.a is not None
    assert triangle_valid.b is not None
    assert triangle_valid.c is not None


def test_triangle_negative(triangle_invalid):
    assert triangle_invalid is None


def test_triangle_attributes():
    a, b, c = 1, 2, 3
    triangle = Triangle(a, b, c)

    assert triangle.perimeter == triangle.a + triangle.b + triangle.c

    s = (triangle.a + triangle.b + triangle.c) / 2
    area = (s*(s-triangle.a)*(s-triangle.b)*(s-triangle.c)) ** 0.5
    assert triangle.area == area


def test_triangle_representation(triangle_valid):
    assert str(triangle_valid) == "{} with sides {}x{}x{}".format(
        triangle_valid.name, triangle_valid.a, triangle_valid.b, triangle_valid.c)


def test_triangle_name(triangle_valid):
    assert triangle_valid.name == "Triangle"


def test_triangle_add_area(triangle_valid, circle_valid):
    assert triangle_valid.add_area(circle_valid) == triangle_valid.area + circle_valid.area


def test_triangle_add_area_negative(triangle_valid):
    with pytest.raises(ValueError):
        triangle_valid.add_area(42)
