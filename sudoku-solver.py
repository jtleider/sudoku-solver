import grid

grids=[]
infile=open('sudoku.txt','r')
while True:
    if infile.readline() == '':
        break
    grids.append([[int(i) for i in infile.readline().strip()] \
                     for j in range(9)])
infile.close()

s = 0
for i in range(len(grids)):
    curGrid = grid.Grid(grids[i])
    curGrid.solve()
    print curGrid
    print curGrid.getCell(0, 0) + curGrid.getCell(0, 1) + curGrid.getCell(0, 2)
    s += int(str(curGrid.getCell(0, 0)) + str(curGrid.getCell(0, 1)) + str(curGrid.getCell(0, 2)))
print s

