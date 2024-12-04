input = [i.strip('\n') for i in open(r'Day 4\input.txt', 'r').readlines()]

def arrayToDict(input):
    grid = {}
    for i, row in enumerate(input):
        for j, value in enumerate(row):
            grid[(i,j)] = value
    return grid

grid = arrayToDict(input)

i=j=0

count = 0

while (i,0) in grid.keys():
    j=0
    while(i,j) in grid.keys():
        if(grid[(i, j)]) == 'A':
            if set([(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]).issubset(set(grid.keys())):
                if set([grid[(i-1, j-1)], grid[(i+1, j+1)]]) == set(['M', 'S']) and set([grid[(i-1, j+1)], grid[(i+1, j-1)]]) == set(['M', 'S']):
                    count+=1
        j+=1
    i+=1
print(count)

