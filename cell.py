from shapes import Line, Point
from window import Window


class Cell:
    def __init__(
        self,
        has_left_wall: bool,
        has_right_wall: bool,
        has_top_wall: bool,
        has_bottom_wall: bool,
        _x1: int,
        _x2: int,
        _y1: int,
        _y2: int,
        _win: Window,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1  # top left x
        self._y1 = _y1  # top left y
        self._x2 = _x2  # bottom right x
        self._y2 = _y2  # bottom right y
        self._win = _win  # window where we acces the canvas to draw things
        self.width = self._x2 - self._x1
        self.height = self._y2 - self._y1

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(x=self._x1, y=self._y1), Point(x=self._x1, y=self._y1))
            self._win.draw_line(line, fill_color="red")

        if self.has_right_wall:
            line = Line(Point(x=self._x2, y=self._y1), Point(x=self._x2, y=self._y1 + self.height))
            self._win.draw_line(line, fill_color="red")

        if self.has_top_wall:
            line = Line(Point(x=self._x1, y=self._y1), Point(x=self._x1 + self.width, y=self._y1))
            self._win.draw_line(line, fill_color="red")

        if self.has_bottom_wall:
            line = Line(Point(x=self._x1, y=self._y2), Point(x=self._x1 + self.width, y=self._y2))
            self._win.draw_line(line, fill_color="red")
