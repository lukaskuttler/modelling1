from color_point import ColorPoint

class AdvancePoint(ColorPoint):
    #Class variables
    COLORS = ["red", "green", "blue", "yellow", "black", "white"]
    def __init__(self, x, y, color):
        #Check the color
        if color not in self.COLORS:
            raise ValueError(f"Invalid color : need to be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value): # this is a SETTER!!
        if value not in self.COLORS:
            raise ValueError(f"Invalid color : need to be one of {self.COLORS}")
        self._color = value




p1 = AdvancePoint(1, 2, "red")
print(p1)
# p2 = AdvancePoint(1, 2, "pink")
print(p1.x)
#p1.x = 3