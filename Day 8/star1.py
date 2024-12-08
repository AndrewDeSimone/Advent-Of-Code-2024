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
        if (pair[0]-pair[1])+pair[0] in map.keys():
            antinodes.append((pair[0]-pair[1])+pair[0])

print(len(set(antinodes)))