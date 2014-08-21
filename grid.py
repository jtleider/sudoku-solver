class Grid:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
	output = ""
	for i in range(9):
		if i % 3 == 0: output = output + "-"*25 + "\n"
		for j in range(9):
			if j % 3 == 0: output = output + "| "
			output = output + str(self.grid[i][j]) + " "
		output = output + "|\n"
	output = output + "-"*25 + "\n"
	return output

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
					if self.grid[i1*3+i2][j1*3+j2] != 0 and self.grid[i1*3+i2][j1*3+j2] in seen:
						return False
					seen.append(self.grid[i1*3+i2][j1*3+j2])
        return True

    def isSolved(self):
        """Is this grid solved?"""
	if not self.isValid():
		return False
	for i in range(9):
		for j in range(9):
			if self.grid[i][j] == 0:
				return False
        return True

    def possibleValues(self, m, n):
        """Return list of possible values for cell in
        row m, column n in grid, where m, n are between
        0 and 8."""
	used = [False for i in range(9+1)]
	for j in range(9):
		if j == n: continue
		used[self.grid[m][j]] = True
	for i in range(9):
		if i == m: continue
		used[self.grid[i][n]] = True
	for i in range(m - (m % 3), m - (m % 3) + 3):
		for j in range(n - (n % 3), n - (n % 3) + 3):
			if i == m and j == n: continue
			used[self.grid[i][j]] = True
        return [i for i in range(1, 9+1) if not used[i]]

    def setCell(self, m, n, value):
        """Set the value of the cell in row m, column n."""
	self.grid[m][n] = value

    def getCell(self, m, n):
	"""Get the value of the cell in row m, column n."""
	return self.grid[m][n]

    def findEmpty(self):
        """Return the row and column of an empty cell in the
        grid, None if the grid is complete."""
	for i in range(9):
		for j in range(9):
			if self.grid[i][j] == 0: return [i, j]
        return None

    def solve(self):
	"""Solve the Sudoku grid. Throw GridException if this is not possible."""
	pass

class GridException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

