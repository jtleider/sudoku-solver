class Grid:
    def __init__(self, grid):
        self.grid = grid

    def isValid(self):
        """Is this a valid Sudoku grid? The grid need not be
        complete, but there should be no problems like a
        duplicate number in a row."""
        # Check each row
        for i in range(9):
            seen = []
            for j in range(9):
                if self.grid[i][j] != 0 and self.grid[i][j] in seen:
                    return False
                seen.append(self.grid[i][j])
        # Check each column
        for j in range(9):
            seen = []
            for i in range(9):
                if self.grid[i][j] != 0 and self.grid[i][j] in seen:
                    return False
                seen.append(self.grid[i][j])
        # Check each sub-grid
        for i1 in range(3):
		for j1 in range(3):
			# Check each of three subgrids, indexed by i1,j1.
			seen = []
			for i2 in range(3):
				for j2 in range(3):
					if self.grid[i1*3+i2][j1*3+j2] != 0 and self.grid[i1*3+i][j1*3+j2] in seen:
						return False
					seen.append(self.grid[i1*3+i2][j1*3+j2])
        return True

    def isSolved(self):
        """Is this grid solved?"""
        pass

    def possibleValues(self, m, n):
        """Return list of possible values for cell in
        row m, column n in grid, where m, n are between
        0 and 8."""
        pass

    def setCell(self, m, n):
        """Set the value of the cell in row m, column n."""
        pass

    def findEmpty(self):
        """Return the row and column of an empty cell in the
        grid, None if the grid is complete."""
        pass
