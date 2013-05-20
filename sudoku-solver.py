import copy

def solve(grid):
    """Solve Sudoku puzzle recursively."""
    mg, status = geniGrid(grid)
    if not status:
        return False
    for i in range(len(mg)):
        for j in range(len(mg[i])):
            if type(mg[i][j]) == type([]):
                if len(mg[i][j]) == 0: return False # no way to do it
                for op in mg[i][j]:
                    newGrid = copy.deepcopy(mg)
                    newGrid[i][j] = op
                    if solve(newGrid):
                        for row in range(len(grid)):
                            for col in range(len(grid[row])):
                                grid[row][col] = newGrid[row][col]
                        return True
                return False # boxed in by previous choices
    return True

def geniGrid(grid):
    """Process grid, place list of options in each unfilled box."""
    notUsedRow = [[k for k in range(1,10)] for j in range(9)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if notUsedRow[row].count(grid[row][col]) > 0:
                del(notUsedRow[row][notUsedRow[row].index(grid[row][col])])
    notUsedCol = [[k for k in range(1,10)] for j in range(9)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if notUsedCol[col].count(grid[row][col]) > 0:
                del(notUsedCol[col][notUsedCol[col].index(grid[row][col])])
    notUsedGrid = [ [ [k for k in range(1,10)] for q in range(3) ] \
                        for j in range(3)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if notUsedGrid[row/3][col/3].count(grid[row][col]) > 0:
                del(notUsedGrid[row/3][col/3][ \
                        notUsedGrid[row/3][col/3].index(grid[row][col])])
    newGrid = [[i for i in range(9)] for i in range(9)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0 or type(grid[row][col]) == type([]):
                newGrid[row][col] = intersect(notUsedRow[row], \
                                                  notUsedCol[col], \
                                                  notUsedGrid[row/3][col/3])
                if newGrid[row][col] == []: return grid, False
            else:
                newGrid[row][col] = grid[row][col]
    return newGrid, True

def tstr(s):
    """Tight string (no spaces in lists)."""
    if type(s) == type(1):
        return str(s)
    else: # list
        ans = '['
        for i in s:
            ans += str(i)
            if i != s[-1]: ans += ','
        ans += ']'
        return ans

def displayGrid(grid):
    """Prettyprinting for Sudoku grid."""
    for row in range(len(grid)):
        if not row % 3:
            print '-'*70
        for col in range(len(grid[row])):
            if not col % 3: print '|',
            print tstr(grid[row][col]).ljust(13),
        print '|'
    print '-' * 70

def intersect(L1, L2, L3):
    """Intersection of lists L1, L2, L3."""
    ans = []
    for i in L1:
        if i in L2 and i in L3:
            ans.append(i)

    return ans

grid=[]
infile=open('sudoku.txt','r')
while True:
    if infile.readline() == '':
        break
    grid.append([[int(i) for i in infile.readline().strip()] \
                     for j in range(9)])
infile.close()

s = 0
for i in range(len(grid)):
    solve(grid[i])
    displayGrid(grid[i])
    print int(str(grid[i][0][0])+str(grid[i][0][1])+str(grid[i][0][2]))
    s += int(str(grid[i][0][0])+str(grid[i][0][1])+str(grid[i][0][2]))
print s
