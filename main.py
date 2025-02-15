from tkinter import Tk, BOTH, Canvas
from shapes import Line, Point


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk(screenName="Maze Solver")
        self.canvas_widget = Canvas(self.root_widget, height=height, width=width)
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


def main():
    win = Window(800, 600)
    win.draw_line(Line(point0=Point(25, 25), point1=Point(50, 50)), fill_color="red")
    win.draw_line(Line(point0=Point(50, 25), point1=Point(25, 50)), fill_color="red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
