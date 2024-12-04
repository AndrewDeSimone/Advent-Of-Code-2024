input = [i.strip('\n') for i in open(r'Day 4\input.txt', 'r').readlines()]

def arrayToDict(input):
    grid = {}
    for i, row in enumerate(input):
        for j, value in enumerate(row):
            grid[(i,j)] = value
    return grid

def findNext(grid, i, j, veci, vecj, letters):
    if letters == []:
        return True
    if (i+veci, j+vecj) not in grid.keys():
        return False
    if grid[(i+veci, j+vecj)] != letters[0]:
        return False
    return findNext(grid, i+veci, j+vecj, veci, vecj, letters[1:])

grid = arrayToDict(input)

i=j=0

count = 0

while (i,0) in grid.keys():
    j=0
    while(i,j) in grid.keys():
        if(grid[(i, j)]) == 'X':
            count += findNext(grid, i, j, -1, -1, ['M', 'A', 'S'])
            count += findNext(grid, i, j, -1, 0, ['M', 'A', 'S'])
            count += findNext(grid, i, j, -1, 1, ['M', 'A', 'S'])
            count += findNext(grid, i, j, 0, -1, ['M', 'A', 'S'])
            count += findNext(grid, i, j, 0, 0, ['M', 'A', 'S'])
            count += findNext(grid, i, j, 0, 1, ['M', 'A', 'S'])
            count += findNext(grid, i, j, 1, -1, ['M', 'A', 'S'])
            count += findNext(grid, i, j, 1, 0, ['M', 'A', 'S'])
            count += findNext(grid, i, j, 1, 1, ['M', 'A', 'S'])
        j+=1
    i+=1
print(count)

