input = [i.split('   ') for i in open(r'Day 1\input.txt', 'r').read().split('\n')]

left = []
right = []

for i in input:
    left.append(int(i[0]))
    right.append(int(i[1]))
left.sort()
right.sort()

print(sum([abs(x-y) for x, y in zip(left, right)]))