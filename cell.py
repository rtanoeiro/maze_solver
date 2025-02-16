from graphics import Window, Point, Line
from typing import Optional
import random

DIRECTION = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


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
        visited=False,
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
        self.visited = visited

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

    def __repr__(self):
        return f"Cell(TopWall: {self.has_top_wall}, BottomWall: {self.has_bottom_wall}, LeftWall: {self.has_left_wall}, RightWall: {self.has_right_wall})"

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
        seed: Optional[int | None] = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells: list[list[Cell]] = []
        self._create_cells()
        self._break_walls_r(0, 0)
        self._break_entrance_exit()

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(self.cells[i][j], i=i, j=j)

        if seed:
            self.seed = random.seed(seed)

    def _create_cells(self):
        for i in range(self.num_rows):
            col_cells = []
            for j in range(self.num_cols):
                cell = Cell(
                    has_left_wall=True,
                    has_right_wall=True,
                    has_top_wall=True,
                    has_bottom_wall=True,
                    _x1=self.x1 + j * self.cell_size_x,
                    _y1=self.y1 + i * self.cell_size_y,
                    _x2=self.x1 + (j + 1) * self.cell_size_x,
                    _y2=self.y1 + (i + 1) * self.cell_size_y,
                    _win=self.win,
                )
                col_cells.append(cell)
            self.cells.append(col_cells)

    def _draw_cell(self, cell: Cell, i, j):
        if self.win is not None:  # only draw if we have a window
            cell.draw()

    def _break_walls_r(self, i, j):
        while True:
            self.cells[i][j].visited = True
            possible_directions = []

            if (i + 1 < self.num_rows) and (not self.cells[i + 1][j].visited):
                possible_directions.append("down")
            if (i - 1 >= 0) and (not self.cells[i - 1][j].visited):
                possible_directions.append("up")
            if (j + 1 < self.num_cols) and (not self.cells[i][j + 1].visited):
                possible_directions.append("right")
            if (j - 1 >= 0) and (not self.cells[i][j - 1].visited):
                possible_directions.append("left")

            if not possible_directions:
                break

            direction = random.choice(possible_directions)
            self.break_wall_directions(direction, i, j)
            self._break_walls_r(i + DIRECTION[direction][0], j + DIRECTION[direction][1])

    def break_wall_directions(self, direction: str, i: int, j: int):
        if direction == "up":
            self.cells[i][j].has_top_wall = False
            self.cells[i - 1][j].has_bottom_wall = False
            return

        if direction == "down":
            self.cells[i][j].has_bottom_wall = False
            self.cells[i + 1][j].has_top_wall = False
            return

        if direction == "left":
            self.cells[i][j].has_left_wall = False
            self.cells[i][j - 1].has_right_wall = False
            return

        if direction == "right":
            self.cells[i][j].has_right_wall = False
            self.cells[i][j + 1].has_left_wall = False
            return

    def _break_entrance_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
