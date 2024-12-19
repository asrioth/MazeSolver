import unittest
from maze import Maze
from point import Point
from cell import Cell
from line import Line
from cell import WallDirection

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(m1._cells[num_cols-1][num_rows-1]._top_left, Point((num_cols-1) * 10, (num_rows-1) * 10))
        m2 = Maze(Point(10, 5), num_rows, num_cols, 10, 10)
        self.assertEqual(m2._cells[num_cols-1][num_rows-1]._top_left, Point((num_cols-1) * 10 + 10, (num_rows-1) * 10 + 5))

    def test_break_entrance_and_exit(self):
        num_cols = 6
        num_rows = 5
        m1 = Maze(Point(), num_rows, num_cols, 10, 10)
        start_broken = m1._cells[0][0].walls[WallDirection.LEFT.value] ^ m1._cells[0][0].walls[WallDirection.TOP.value]
        end_broken = m1._cells[-1][-1].walls[WallDirection.RIGHT.value] ^ m1._cells[-1][-1].walls[WallDirection.BOTTOM.value]
        self.assertTrue(start_broken)
        self.assertTrue(end_broken)

    def test_get_neighbours(self):
        num_cols = 8
        num_rows = 8
        m1 = Maze(Point(), num_rows, num_cols, 10, 10)
        neighbours = m1._get_neighbours(0, 7)
        expected_neighbours = [(1, 7, WallDirection.RIGHT), (0, 6, WallDirection.TOP)]
        self.assertEqual(neighbours, expected_neighbours)
        neighbours = m1._get_neighbours(7, 0)
        expected_neighbours = [(6, 0, WallDirection.LEFT), (7, 1, WallDirection.BOTTOM)]
        self.assertEqual(neighbours, expected_neighbours)
        neighbours = m1._get_neighbours(4, 4)
        self.assertEqual(len(neighbours), 4)

    def test_break_wall(self):
        num_cols = 8
        num_rows = 8
        m1 = Maze(Point(), num_rows, num_cols, 10, 10)
        neighbours = m1._get_neighbours(4,4)
        i = 0
        m1._break_wall(neighbours[i], 4, 4)
        self.assertFalse(m1._cells[4][4].walls[neighbours[i][2].value])
        self.assertFalse(m1._cells[neighbours[i][0]][neighbours[i][1]].walls[WallDirection.RIGHT.value])
        i = 1
        m1._break_wall(neighbours[i], 4, 4)
        self.assertFalse(m1._cells[4][4].walls[neighbours[i][2].value])
        self.assertFalse(m1._cells[neighbours[i][0]][neighbours[i][1]].walls[WallDirection.LEFT.value])
        i = 2
        m1._break_wall(neighbours[i], 4, 4)
        self.assertFalse(m1._cells[4][4].walls[neighbours[i][2].value])
        self.assertFalse(m1._cells[neighbours[i][0]][neighbours[i][1]].walls[WallDirection.BOTTOM.value])
        i = 3
        m1._break_wall(neighbours[i], 4, 4)
        self.assertFalse(m1._cells[4][4].walls[neighbours[i][2].value])
        self.assertFalse(m1._cells[neighbours[i][0]][neighbours[i][1]].walls[WallDirection.TOP.value])

    def test_reset_cells_visited(self):
        num_cols = 8
        num_rows = 8
        m1 = Maze(Point(), num_rows, num_cols, 10, 10)
        m1._break_walls_r(0, 0)
        self.assertTrue(m1._cells[4][4].visited)
        m1._reset_cells_visited()
        self.assertFalse(m1._cells[4][4].visited)



if __name__ == "__main__":
    unittest.main()