from window import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell = Cell(
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
        _x1=1,
        _y1=1,
        _x2=100,
        _y2=100,
        _win=win,
    )
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
