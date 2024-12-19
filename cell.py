from point import Point
from line import Line
from window import Window

class Cell():
    def __init__(self, top_left, bottom_right, walls = [True,True,True,True], window = None):
        self.has_left_wall = walls[0]
        self.has_right_wall = walls[1]
        self.has_top_wall = walls[2]
        self.has_bottom_wall = walls[3]
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._window = window

    def draw(self):
        lines = self.make_cell_lines()
        for line in lines:
            self._window.draw_line(line, "Black")

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
        if self.has_left_wall:
            lines.append(Line(self._top_left, Point(self._top_left.x, self._bottom_right.y)))
        if self.has_right_wall:
            lines.append(Line(Point(self._bottom_right.x, self._top_left.y), self._bottom_right))
        if self.has_top_wall:
            lines.append(Line(self._top_left, Point(self._bottom_right.x, self._top_left.y)))
        if self.has_bottom_wall:
            lines.append(Line(Point(self._top_left.x, self._bottom_right.y), self._bottom_right))
        return lines
    
    def __repr__(self):
        return f"Cell({self._top_left}, {self._bottom_right}, [{self.has_left_wall}, {self.has_right_wall}, {self.has_top_wall}, {self.has_bottom_wall}])"