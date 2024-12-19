from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(0, 0), Point(380, 265))
    line2 = Line(Point(0, 265), Point(380, 0))
    win.draw_line(line1, "yellow")
    win.draw_line(line2, "purple")
    win.wait_for_close()

if __name__ == "__main__":
    main()