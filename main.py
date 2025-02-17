from graphics import Window
from cell import Maze


def main():
    win = Window(1000, 800)
    maze = Maze(x1=50, y1=50, num_rows=12, num_cols=12, cell_size_x=50, cell_size_y=50, win=win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
