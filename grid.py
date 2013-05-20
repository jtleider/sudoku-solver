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
        pass
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
