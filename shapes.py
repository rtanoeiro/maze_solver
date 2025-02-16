from tkinter import Canvas


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
            self.point0.x,
            self.point0.y,
            self.point1.x,
            self.point1.y,
            fill=fill_color,
            width=5,
        )
