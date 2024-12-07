input = open(r'Day 6\input.txt', 'r').readlines()

factory = {}
position = 0
direction = -1

for i, value in enumerate(input):
    for j, value in enumerate(value):
        if(value == '\n'):
            continue
        if(value == '^'):
            factory[i + j*(1j)] = '.'
            position = i + j*(1j)
        else:
            factory[i + j*(1j)] = value

startpos = position
startdir = direction

seen = []

while True:
    seen.append(position)
    if position+direction not in factory.keys():
        break
    if factory[position+direction] == '#':
        direction *= -1j
    else:
        position += direction

searchSpace = set(seen)

def loops(factory, block, position, direction):
    dposition = position
    ddirection = direction
    while True:
        moved = 0
        while moved < 2:
            if dposition+ddirection not in factory.keys():
                return False
            if factory[dposition+ddirection] == '#' or dposition+ddirection == block:
                ddirection *= -1j
            else:
                moved += 1
                dposition += ddirection
        moved = 0
        while moved < 1:
            if position+direction not in factory.keys():
                return False
            if factory[position+direction] == '#' or position+direction == block:
                direction *= -1j
            else:
                moved += 1
                position += direction
        if position == dposition and direction == ddirection:
            return True
        


count = 0
for i in searchSpace:
    count += loops(factory, i, startpos, startdir)

print(count)