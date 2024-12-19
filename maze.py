from cell import Cell
from point import Point
import time

class Maze():
    def __init__(self, point, num_rows, num_cols, cell_size_x, cell_size_y, window = None):
        self.point = point
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        current_point = Point()
        for i in range(self.num_cols):
            self._cells.append([])
            current_point.x = self.point.x + self.cell_size_x * i
            for j in range(self.num_rows):
                current_point.y = self.point.y + self.cell_size_y * j
                self._cells[i].append(Cell(Point(current_point.x, current_point.y), Point(current_point.x + self.cell_size_x, current_point.y + self.cell_size_y), window=self.window))
        if self.window != None:
            self._draw_cells()
    
    def _draw_cells(self):
        print(self._cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].draw()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)



        