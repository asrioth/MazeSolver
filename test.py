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



if __name__ == "__main__":
    unittest.main()