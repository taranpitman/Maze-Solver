import unittest
from maze import Maze
from graphics import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0,0,num_rows,num_cols,10,10, win)
        self.assertEqual(len(m1._cells),num_cols)
        self.assertEqual(len(m1._cells[0]),num_rows)
    
    def break_entrance_and_exit(self):
        pass




if __name__ == "__main__":
    unittest.main()
#so this triggers all the tests through the unittest import