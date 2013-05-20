import unittest
from grid import Grid

class GridTest(unittest.TestCase):

    def test_isValid_accepts_empty(self):
        grid = Grid([[0 for j in range(9)] for i in range(9)])
        self.assertTrue(grid.isValid())

    def test_isValid_finds_duplicate_row(self):
        grid = Grid([ [0 for j in range(9)] for i in range(8) ] + \
                        [ [1, 0, 0, 0, 0, 1, 2, 2, 2] ])
        self.assertFalse(grid.isValid())

    def test_isValid_finds_duplicate_col(self):
        grid = Grid([ [ [1, 0, 0, 0, 0, 0, 0, 0, 0] ] + \
                          [ [0 for j in range(9)] for i in range(7)] + \
                          [ [1, 0, 0, 0, 0, 0, 0, 0, 0] ] ])
        self.assertFalse(grid.isValid())

if __name__ == '__main__':
    unittest.main()
