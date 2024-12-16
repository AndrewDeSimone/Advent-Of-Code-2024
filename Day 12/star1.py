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

def neighbors(plot, region):
    count = 0
    for direction in [-1, 1, -1j, 1j]:
        if plot+direction in region:
            count += 1
    return count

def perimeter(region):
    sum = 0
    for plot in region:
        sum += 4-neighbors(plot, region)
    return sum

sum = 0
for region in regions:
    sum += area(region) * perimeter(region)

print(sum)