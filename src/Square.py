from src.Figure import Figure

class Square(Figure):

    def __init__(self, a) -> None:
        self.a = a
    
    def figure_is_valid(a):
        return a > 0

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4

    def __repr__(self):
        return "{0} with sides {1}x{1}x{1}x{1}".format(self.name, self.a)
