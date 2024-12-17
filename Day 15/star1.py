input = open(r'Day 15\input.txt', 'r').read().split('\n\n')

grid = input[0].split('\n')
instructions = input[1]
directions = {'<': -1, '^': -1j, '>': 1, 'v': 1j}

gridMap = {}
robot = 0

for i, row in enumerate(grid):
    for j, value in enumerate(row):
        if value == '.':
            continue
        gridMap[j+i*1j] = value
        if value == '@':
            robot = j+i*1j

def move(item, gridMap, direction):
    if item not in gridMap.keys():
        return item, gridMap, True
    if gridMap[item] in ['@', 'O']:
        _, gridMap, movable = move(item+direction, gridMap, direction)
        gridMap[item + direction*movable] = gridMap.pop(item)
        return item + direction*movable, gridMap, movable
    if gridMap[item] == '#':
        return item, gridMap, False

for i in instructions:
    if i == '\n':
        continue
    robot, gridMap, _ = move(robot, gridMap, directions[i])

total = 0
for i in gridMap.keys():
    if gridMap[i] == 'O':
        total += int(i.real) + 100 * int(i.imag)

print(total)