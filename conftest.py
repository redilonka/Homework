import pytest

from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle

@pytest.fixture
def circle_valid():
    return Circle(5)


@pytest.fixture
def circle_invalid():
    return Circle(0)


@pytest.fixture
def triangle_valid():
    return Triangle(2, 2, 4)


@pytest.fixture
def triangle_invalid():
    return Triangle(2, 2, -1)


@pytest.fixture
def square_valid():
    return Square(2)


@pytest.fixture
def square_invalid():
    return Square(0)


@pytest.fixture
def rectangle_valid():
    return Rectangle(2, 2)


@pytest.fixture
def rectangle_invalid():
    return Rectangle(2, -2)
