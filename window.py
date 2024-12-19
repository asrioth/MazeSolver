from tkinter import Tk, BOTH, Canvas
from line import Line


class Window():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Maze Solver")
        self.root.config(bg = "white")
        self.canvas = Canvas(self.root, width = width, height= height, bg = "White")
        Canvas.pack(self.canvas, fill="both")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill):
        line.draw(self.canvas, fill)