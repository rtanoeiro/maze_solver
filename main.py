from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk().title("Maze Solver")
        self.canvas_widget = Canvas().pack()
        self.is_running = False
