input = open(r'Day 15\input.txt', 'r').read().split('\n\n')

grid = input[0].split('\n')
instructions = input[1]
directions = {'<': -1, '^': -1j, '>': 1, 'v': 1j}

gridMap = {}
robot = 0

for i, row in enumerate(grid):
    for j, value in enumerate(row):
        gridMap[j+i*1j] = value
        if value == '@':
            robot = j+i*1j

def move(robot, gridMap, direction):
    #handle trivial moves
    if gridMap[robot+direction] == '.':
        gridMap[robot] = '.'
        gridMap[robot+direction] = '@'
        robot = robot + direction
        return robot, gridMap
    #next to barrier
    if gridMap[robot+direction] != '#':
        #check movable
        temp = robot
        while True:
            temp += direction
            if gridMap[temp] == '#':
                return robot, gridMap
            if gridMap[temp] == '.':
                break
        while temp != robot+direction:
            gridMap[temp] = 'O'
            temp -= direction
        gridMap[robot+direction] = '@'
        gridMap[robot] = '.'
        return robot+direction, gridMap
    return robot, gridMap

for i in instructions:
    if i == '\n':
        continue
    robot, gridMap = move(robot, gridMap, directions[i])

total = 0
for i in gridMap.keys():
    if gridMap[i] == 'O':
        total += int(i.real) + 100 * int(i.imag)

print(total)