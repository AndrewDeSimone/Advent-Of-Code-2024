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

seen = []

while True:
    seen.append(position)
    if position+direction not in factory.keys():
        break
    if factory[position+direction] == '#':
        direction *= -1j
    else:
        position += direction

print(len(set(seen)))