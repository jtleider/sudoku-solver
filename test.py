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

    def test_isValid_finds_duplicate_sgrid(self):
	grid = Grid([[1, 2, 3,  4, 5, 6,  7, 8, 9]] +
			[[2, 3, 4,  5, 6, 7,  8, 9, 0]] +
			[[3, 4, 5,  6, 7, 8,  9, 0, 1]] +
			[[4, 5, 6,  7, 8, 9,  0, 1, 2]] +
			[[5, 6, 7,  8, 9, 0,  1, 2, 3]] +
			[[6, 7, 8,  9, 0, 1,  2, 3, 4]] +
			[[7, 8, 9,  0, 1, 2,  3, 4, 5]] +
			[[8, 9, 0,  1, 2, 3,  4, 5, 6]] +
			[[9, 0, 1,  2, 3, 4,  5, 6, 7]])
	self.assertFalse(grid.isValid())
	grid = Grid([[1, 0, 0, 0, 0, 0, 0, 0, 0]] +
			[[0, 1, 0, 0, 0, 0, 0, 0, 0]] +
			[[0 for j in range(9)] for i in range(7)])
	self.assertFalse(grid.isValid())

    def test_isValid_accepts_solved(self):
	grid = Grid([[9, 6, 3, 1, 7, 4, 2, 5, 8]]+
			[[1, 7, 8, 3, 2, 5, 6, 4, 9]] +
			[[2, 5, 4, 6, 8, 9, 7, 3, 1]] +
			[[8, 2, 1, 4, 3, 7, 5, 9, 6]] +
			[[4, 9, 6, 8, 5, 2, 3, 1, 7]] +
			[[7, 3, 5, 9, 6, 1, 8, 2, 4]] +
			[[5, 8, 9, 7, 1, 3, 4, 6, 2]] +
			[[3, 1, 7, 2, 4, 6, 9, 8, 5]] +
			[[6, 4, 2, 5, 9, 8, 1, 7, 3]])
	self.assertTrue(grid.isValid())
	

    def test_isSolved(self):
	grid = Grid([[9, 6, 3, 1, 7, 4, 2, 5, 8]]+
			[[1, 7, 8, 3, 2, 5, 6, 4, 9]] +
			[[2, 5, 4, 6, 8, 9, 7, 3, 1]] +
			[[8, 2, 1, 4, 3, 7, 5, 9, 6]] +
			[[4, 9, 6, 8, 5, 2, 3, 1, 7]] +
			[[7, 3, 5, 9, 6, 1, 8, 2, 4]] +
			[[5, 8, 9, 7, 1, 3, 4, 6, 2]] +
			[[3, 1, 7, 2, 4, 6, 9, 8, 5]] +
			[[6, 4, 2, 5, 9, 8, 1, 7, 3]])
	self.assertTrue(grid.isSolved())
	grid = Grid([[0, 6, 3, 1, 7, 4, 2, 5, 8]]+
			[[1, 7, 8, 3, 2, 5, 6, 4, 9]] +
			[[2, 5, 4, 6, 8, 9, 7, 3, 1]] +
			[[8, 2, 1, 4, 3, 7, 5, 9, 6]] +
			[[4, 9, 6, 8, 5, 2, 3, 1, 7]] +
			[[7, 3, 5, 9, 6, 1, 8, 2, 4]] +
			[[5, 8, 9, 7, 1, 3, 4, 6, 2]] +
			[[3, 1, 7, 2, 4, 6, 9, 8, 5]] +
			[[6, 4, 2, 5, 9, 8, 1, 7, 3]])
	self.assertFalse(grid.isSolved())
	grid = Grid([[9, 6, 3, 1, 7, 4, 2, 5, 8]]+
			[[1, 7, 9, 3, 2, 5, 6, 4, 9]] +
			[[2, 5, 4, 6, 8, 9, 7, 3, 1]] +
			[[8, 2, 1, 4, 3, 7, 5, 9, 6]] +
			[[4, 9, 6, 8, 5, 2, 3, 1, 7]] +
			[[7, 3, 5, 9, 6, 1, 8, 2, 4]] +
			[[5, 8, 9, 7, 1, 3, 4, 6, 2]] +
			[[3, 1, 7, 2, 4, 6, 9, 8, 5]] +
			[[6, 4, 2, 5, 9, 8, 1, 7, 3]])
	self.assertFalse(grid.isSolved())

    def test_possibleValues(self):
	grid = Grid([[9, 6, 3, 1, 7, 4, 2, 5, 8]]+
			[[1, 7, 8, 3, 2, 5, 6, 4, 9]] +
			[[2, 5, 4, 6, 8, 9, 7, 3, 1]] +
			[[8, 2, 1, 4, 3, 7, 5, 9, 6]] +
			[[4, 9, 6, 8, 5, 2, 3, 1, 7]] +
			[[7, 3, 5, 9, 6, 1, 8, 2, 4]] +
			[[5, 8, 9, 7, 1, 3, 4, 6, 2]] +
			[[3, 1, 7, 2, 4, 6, 9, 8, 5]] +
			[[6, 4, 2, 5, 9, 8, 1, 7, 3]])
	self.assertEqual(grid.possibleValues(1, 2), [8])
	grid = Grid([[0, 6, 3, 1, 0, 4, 2, 5, 8]]+
			[[1, 0, 8, 3, 2, 5, 6, 4, 9]] +
			[[2, 5, 4, 6, 8, 9, 7, 3, 1]] +
			[[8, 2, 1, 4, 3, 7, 5, 9, 6]] +
			[[4, 0, 6, 8, 5, 2, 3, 1, 7]] +
			[[7, 3, 5, 9, 6, 1, 8, 2, 4]] +
			[[5, 8, 9, 7, 1, 3, 4, 6, 2]] +
			[[3, 1, 7, 2, 4, 6, 9, 8, 5]] +
			[[6, 4, 2, 5, 9, 8, 1, 7, 3]])
	self.assertEqual(grid.possibleValues(0, 1), [6, 7, 9])
	
if __name__ == '__main__':
    unittest.main()
