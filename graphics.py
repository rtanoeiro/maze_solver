from tkinter import BOTH, Canvas, Tk


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point0: Point, point1: Point):
        self.point0 = point0
        self.point1 = point1

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point0.x, self.point0.y, self.point1.x, self.point1.y, fill=fill_color, width=5
        )


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk(screenName="Maze Solver")
        self.canvas_widget = Canvas(
            self.root_widget, height=height, width=width, background="white"
        )
        self.canvas_widget.pack(fill=BOTH, expand=True)
        self.is_running = False

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def draw_line(self, line: Line, fill_color: str):
        line.draw(canvas=self.canvas_widget, fill_color=fill_color)

    def close(self):
        self.is_running = False
        self.root_widget.destroy()
