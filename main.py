from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

#    line1 = Line(Point(0, 0), Point(380, 265))
#    line2 = Line(Point(0, 265), Point(380, 0))

def main():
    win = Window(800, 600)
    maze = Maze(Point(25, 25), 11, 15, 50, 50, win)
    """cell1 = Cell(win, [True, True, True, True])
    cell2 = Cell(win, [True, True, True, False])
    cell3 = Cell(win, [True, True, False, False])
    cell4 = Cell(win, [True, False, False, False])
    cell5 = Cell(win, [False, True, False, False])
    cell1.draw(Point(10, 50), Point(60, 100))
    cell2.draw(Point(40, 50), Point(60, 70))
    cell3.draw(Point(80, 50), Point(100, 70))
    cell4.draw(Point(120, 50), Point(140, 70))
    cell5.draw(Point(160, 50), Point(180, 70))
    cell1.draw_move(cell2)
    cell3.draw_move(cell4, True)"""
    win.wait_for_close()

if __name__ == "__main__":
    main()