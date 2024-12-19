from cell import Cell
from point import Point
import time

class Maze():
    def __init__(self, point, num_rows, num_cols, cell_size_x, cell_size_y, window):
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
            current_point.y = self.point.y + self.cell_size_y * i
            for j in range(self.num_rows):
                current_point.x = self.point.x + self.cell_size_x * j
                self._cells[i].append(Cell(self.window, current_point, Point(current_point.x + self.cell_size_x, current_point.y + self.cell_size_y)))
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)



        