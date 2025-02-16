from graphics import Window, Point, Line
import time
from typing import Optional


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
        _win: Optional[Window | None] = None,
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
            line = Line(Point(x=self._x1, y=self._y1), Point(x=self._x1, y=self._y2))
            self._win.draw_line(line, fill_color="red")

        if self.has_right_wall:
            line = Line(Point(x=self._x2, y=self._y1), Point(x=self._x2, y=self._y2))
            self._win.draw_line(line, fill_color="red")

        if self.has_top_wall:
            line = Line(Point(x=self._x1, y=self._y1), Point(x=self._x2, y=self._y1))
            self._win.draw_line(line, fill_color="red")

        if self.has_bottom_wall:
            line = Line(Point(x=self._x1, y=self._y2), Point(x=self._x2, y=self._y2))
            self._win.draw_line(line, fill_color="red")

    def draw_move(self, to_cell: "Cell", undo=False):
        if undo:
            color = "red"
        else:
            color = "gray"

        starting_x, starting_y = self._x1 + self.width / 2, self._y1 + self.height / 2
        ending_x, ending_y = to_cell._x1 + to_cell.width / 2, to_cell._y1 + to_cell.height / 2

        line = Line(Point(starting_x, starting_y), Point(ending_x, ending_y))
        self._win.draw_line(line, fill_color=color)


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Optional[Window | None] = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                cell = Cell(
                    has_left_wall=True,
                    has_right_wall=True,
                    has_top_wall=True,
                    has_bottom_wall=True,
                    _x1=self.x1 + i * self.cell_size_x,
                    _y1=self.y1 + j * self.cell_size_y,
                    _x2=self.x1 + (i + 1) * self.cell_size_x,
                    _y2=self.y1 + (j + 1) * self.cell_size_y,
                    _win=self.win,
                )
                col_cells.append(cell)
            self.cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(self.cells[i][j])

    def _draw_cell(self, cell: Cell):
        if self.win is not None:  # only draw if we have a window
            cell.draw()
            self._animate()

    def _animate(self):
        time.sleep(0.1)
