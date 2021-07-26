import pytest
import math

from src.Circle import Circle


def test_circle_init_positive(circle_valid):
    assert circle_valid.r is not None


def test_circle_negative(circle_invalid):
    assert circle_invalid is None


def test_circle_attributes():
    radius = 5
    circle = Circle(radius)

    assert circle.perimeter == 2 * math.pi * radius
    assert circle.area == math.pi * (radius ** 2)


def test_circle_representation(circle_valid):
    assert str(circle_valid) == "{} with radius {}".format(
        circle_valid.name, circle_valid.r)


def test_circle_name(circle_valid):
    assert circle_valid.name == "Circle"


def test_circle_add_area(circle_valid, triangle_valid):
    assert circle_valid.add_area(triangle_valid) == circle_valid.area + triangle_valid.area


def test_circle_add_area_negative(circle_valid):
    with pytest.raises(ValueError):
        circle_valid.add_area(42)
