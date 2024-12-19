import unittest
from maze import Maze
from point import Point
from cell import Cell
from line import Line

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


if __name__ == "__main__":
    unittest.main()