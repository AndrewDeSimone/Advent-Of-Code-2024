input = [i.split('   ') for i in open(r'Day 1\input.txt', 'r').read().split('\n')]

left = []
right = []

for i in input:
    left.append(int(i[0]))
    right.append(int(i[1]))

dict = {}

for i in right:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

sum = 0
for i in left:
    if i in dict.keys():
        sum += i * dict[i]

print(sum)