import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        start = m1._cells[0][0]
        end = m1._cells[-1][-1]
        self.assertEqual(
            start.has_top_wall or
            start.has_bottom_wall or
            start.has_left_wall or
            start.has_right_wall or
            end.has_top_wall or
            end.has_bottom_wall or
            end.has_left_wall or
            end.has_right_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()