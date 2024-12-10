input = [i.strip('\n') for i in open(r'Day 10\input.txt', 'r').readlines()]

topo = {}
trailheads = []

for i, row in enumerate(input):
    for j, value in enumerate(row):
        topo[i+j*1j] = int(value)
        if value == '0':
            trailheads.append(i+j*1j)

def reachablePeaks(trailhead, topo):
    if topo[trailhead] == 9:
        return [trailhead]
    reachable = []
    for direction in [-1, -1j, 1, 1j]:
        if trailhead + direction in topo.keys() and topo[trailhead + direction] - 1 == topo[trailhead]:
            reachable += reachablePeaks(trailhead + direction, topo)
    return reachable

score = 0
for trailhead in trailheads:
    score += len(set(reachablePeaks(trailhead, topo)))

print(score)