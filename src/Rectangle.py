from src.Figure import Figure

class Rectangle(Figure):

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def figure_is_valid(a, b):
        return a > 0 and b > 0

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2

    def __repr__(self):
        return "{} with sides {}x{}".format(self.name, self.a, self.b)
