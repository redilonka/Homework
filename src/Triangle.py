from src.Figure import Figure

class Triangle(Figure):

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def figure_is_valid(a, b, c):
        return a > 0 and b > 0 and c > 0

    @property
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

        if type(area) is complex:
            area = area.real

        return area

    @property
    def perimeter(self):
        """
        Triangle perimeter.
        """
        return self.a + self.b + self.c

    def __repr__(self):
        return "{} with sides {}x{}x{}".format(self.name, self.a, self.b, self.c)
