from point import Point
from line import Line
from window import Window
from enum import Enum

class WallDirection(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3

class Cell():
    def __init__(self, top_left, bottom_right, walls = None, window = None):
        self.walls = walls
        if walls == None:
            self.walls = [True for i in range(4)]
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._window = window

    def draw(self):
        lines, blank_lines = self.make_cell_lines()
        for line in lines:
            self._window.draw_line(line, "Black")
        for line in blank_lines:
            self._window.draw_line(line, "white")

    def draw_move(self, to_cell, undo = False):
        colour = "red"
        if undo:
            colour = "gray"
        joining_line = Line(self.get_center(), to_cell.get_center())
        self._window.draw_line(joining_line, colour)
    
    def get_center(self):
        if self._top_left == None or self._bottom_right == None:
            raise Exception("cell must have valid top and bottom points, before it's center can be retrieved")
        center_x = (self._top_left.x + self._bottom_right.x) / 2
        center_y = (self._top_left.y + self._bottom_right.y) / 2
        return Point(center_x, center_y)

    def make_cell_lines(self):
        lines = []
        blank_lines = []
        left_line = Line(self._top_left, Point(self._top_left.x, self._bottom_right.y))
        right_line = Line(Point(self._bottom_right.x, self._top_left.y), self._bottom_right)
        top_line = Line(self._top_left, Point(self._bottom_right.x, self._top_left.y))
        bottom_line = Line(Point(self._top_left.x, self._bottom_right.y), self._bottom_right)
        if self.walls[WallDirection.LEFT.value]:
            lines.append(left_line)
        else:
            blank_lines.append(left_line)
        if self.walls[WallDirection.RIGHT.value]:
            lines.append(right_line)
        else:
            blank_lines.append(right_line)
        if self.walls[WallDirection.TOP.value]:
            lines.append(top_line)
        else:
            blank_lines.append(top_line)
        if self.walls[WallDirection.BOTTOM.value]:
            lines.append(bottom_line)
        else:
            blank_lines.append(bottom_line)
        return lines, blank_lines
    
    def __repr__(self):
        return f"Cell({self._top_left}, {self._bottom_right}, [{self.has_left_wall}, {self.has_right_wall}, {self.has_top_wall}, {self.has_bottom_wall}])"