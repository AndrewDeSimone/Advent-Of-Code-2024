input = [i.strip('\n') for i in open(r'Day 7\input.txt', 'r').readlines()]

def possible(goal, values, current):
    if len(values) == 0:
        return goal == current
    return possible(goal, values[1:], current + values[0]) or possible(goal, values[1:], current * values[0]) or possible(goal, values[1:], int(str(current) + str(values[0])))


sum = 0
for i in input:
    testValue = int(i.split(':')[0])
    values = [int(j) for j in i.split(':')[1].split()]
    if possible(testValue, values[1:], values[0]):
        sum += testValue

print(sum)