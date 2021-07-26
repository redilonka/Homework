class Figure():
    def __new__(cls, *args):
        """
        Check if figure is creatable.
        """
        if not cls.figure_is_valid(*args):
            return None

        return super().__new__(cls)

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, figure) -> int:
        if not issubclass(type(figure), Figure):
            raise ValueError("Wrong figure's class")
 
        return self.area + figure.area
