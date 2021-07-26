import math

from src.Figure import Figure

class Circle(Figure):

    def __init__(self, r) -> None:
        self.r = r
    
    def figure_is_valid(r):
        return r > 0

    @property
    def area(self):
        return math.pi * (self.r ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def __repr__(self):
        return "{} with radius {}".format(self.name, self.r)
