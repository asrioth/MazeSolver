from cell import Cell, WallDirection
from point import Point
import time
import random

class Maze():
    def __init__(self, point, num_rows, num_cols, cell_size_x, cell_size_y, window = None, seed = None):
        self.point = point
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(random.randrange(0, num_cols), random.randrange(0, num_rows))
        self._reset_cells_visited()
    
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
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].walls[random.choice([WallDirection.LEFT.value, WallDirection.TOP.value])] = False
        self._cells[-1][-1].walls[random.choice([WallDirection.RIGHT.value, WallDirection.BOTTOM.value])] = False
        if self.window != None:
            self._draw_cell(0, 0)
            self._draw_cell(-1, -1)

    def _animate(self):
        self.window.redraw()
        time.sleep(0.005)

    def _get_neighbours(self, i, j):
        neighbours = []
        if i != 0:
            neighbours.append((i-1, j, WallDirection.LEFT))
        if i != len(self._cells)-1:
            neighbours.append((i+1, j, WallDirection.RIGHT))
        if j != 0:
            neighbours.append((i,j-1, WallDirection.TOP))
        if j != len(self._cells[i])-1:
            neighbours.append((i, j+1, WallDirection.BOTTOM))
        return neighbours

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            neighbours = self._get_neighbours(i, j)
            for neighbour in neighbours:
                if not self._cells[neighbour[0]][neighbour[1]].visited:
                    to_visit.append(neighbour)
            if to_visit == []:
                if self.window != None:
                    self._draw_cell(i, j)
                return
            direction = random.choice(to_visit)
            self._break_wall(direction, i, j)
            self._break_walls_r(direction[0], direction[1])
    
    def _break_wall(self, direction, i, j):
        match direction[2]:
            case WallDirection.LEFT:
                self._cells[i][j].walls[WallDirection.LEFT.value] = False
                self._cells[direction[0]][direction[1]].walls[WallDirection.RIGHT.value] = False
            case WallDirection.RIGHT:
                self._cells[i][j].walls[WallDirection.RIGHT.value] = False
                self._cells[direction[0]][direction[1]].walls[WallDirection.LEFT.value] = False
            case WallDirection.TOP:
                self._cells[i][j].walls[WallDirection.TOP.value] = False
                self._cells[direction[0]][direction[1]].walls[WallDirection.BOTTOM.value] = False
            case WallDirection.BOTTOM:
                self._cells[i][j].walls[WallDirection.BOTTOM.value] = False
                self._cells[direction[0]][direction[1]].walls[WallDirection.TOP.value] = False
            case _:
                raise Exception("wall direction not recognised")

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False