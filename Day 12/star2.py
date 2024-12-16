input = [i.strip('\n') for i in open(r'Day 12\input.txt', 'r').readlines()]

grid = {}
toPlace = set()

for i, row in enumerate(input):
    for j, value in enumerate(row):
        grid[i+j*1j] = value
        toPlace.add(i+j*1j)

def fill(grid, start, seen):
    for direction in [-1, 1, -1j, 1j]:
        if start+direction in grid.keys() and grid[start] == grid[start+direction]:
            if start+direction not in seen:
                seen.add(start+direction)
                seen.update(fill(grid, start+direction, seen))
    return seen

regions = []
while len(toPlace) > 0:
    regions.append(fill(grid, list(toPlace)[0], {list(toPlace)[0]}))
    toPlace -= regions[-1]

def area(region):
    return len(region)

def corners(plot, region):
    count = 0
    for direction in [-1, 1, -1j, 1j]:
        if plot+direction not in region and plot+direction*1j not in region:
            count += 1
        if plot+direction in region and plot+direction*1j in region and plot+direction+direction*1j not in region:
            count += 1
    return count
    

def sides(region):
    total = 0
    for plot in region:
        total += corners(plot, region)
    return total

sum = 0
for region in regions:
    sum += area(region) * sides(region)

print(sum)