import pytest

from src.Square import Square


def test_square_init_positive(square_valid):
    assert square_valid.a is not None


def test_square_negative(square_invalid):
    assert square_invalid is None


def test_square_attributes():
    side = 5
    square = Square(side)

    assert square.perimeter == side * 4
    assert square.area == side ** 2


def test_square_representation(square_valid):
    assert str(square_valid) == "{0} with sides {1}x{1}x{1}x{1}".format(
        square_valid.name, square_valid.a)


def test_square_name(square_valid):
    assert square_valid.name == "Square"


def test_square_add_area(square_valid, triangle_valid):
    assert square_valid.add_area(triangle_valid) == square_valid.area + triangle_valid.area


def test_square_add_area_negative(square_valid):
    with pytest.raises(ValueError):
        square_valid.add_area(42)
