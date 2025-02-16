from graphics import Window
from cell import Maze


def main():
    win = Window(800, 600)
    Maze(x1=50, y1=50, num_rows=7, num_cols=5, cell_size_x=100, cell_size_y=100, win=win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
