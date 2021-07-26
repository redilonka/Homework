import pytest

from src.Rectangle import Rectangle


def test_rectangle_init_positive(rectangle_valid):
    assert rectangle_valid.a is not None
    assert rectangle_valid.b is not None


def test_rectangle_negative(rectangle_invalid):
    assert rectangle_invalid is None


def test_rectangle_attributes():
    a, b = 1, 2
    rectangle = Rectangle(a, b)

    assert rectangle.perimeter == (a + b) * 2
    assert rectangle.area == a * b


def test_rectangle_representation(rectangle_valid):
    assert str(rectangle_valid) == "{} with sides {}x{}".format(
        rectangle_valid.name, rectangle_valid.a, rectangle_valid.b)


def test_rectangle_name(rectangle_valid):
    assert rectangle_valid.name == "Rectangle"


def test_rectangle_add_area(rectangle_valid, triangle_valid):
    assert rectangle_valid.add_area(triangle_valid) == rectangle_valid.area + triangle_valid.area


def test_rectangle_add_area_negative(rectangle_valid):
    with pytest.raises(ValueError):
        rectangle_valid.add_area(42)
