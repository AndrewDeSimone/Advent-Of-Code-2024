from itertools import permutations

input = [i.strip('\n') for i in  open(r'Day 8\input.txt').readlines()]

signals = {}
map = {}

for i, row in enumerate(input):
    for j, value in enumerate(row):
        map[i+j*1j] = value
        if value in signals.keys():
            signals[value].append(i+j*1j)
        else:
            signals[value] = [i+j*1j]

signals.pop('.')

antinodes = []
for signal in signals.keys():
    for pair in permutations(signals[signal], 2):
        antinodes.append(pair[0])
        antinodes.append(pair[1])
        difference = pair[0]-pair[1]
        position = pair[0]
        while (difference)+position in map.keys():
            position = (difference)+position
            antinodes.append(position)

print(len(set(antinodes)))