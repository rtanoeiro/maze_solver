from graphics import Window
from cell import Maze


def main():
    win = Window(1600, 1000)
    Maze(x1=50, y1=50, num_rows=16, num_cols=22, cell_size_x=50, cell_size_y=50, win=win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
