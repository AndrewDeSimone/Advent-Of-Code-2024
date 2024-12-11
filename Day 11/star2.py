input = open(r'Day 11\input.txt', 'r').read().split()

state = {}
for i in input:
    if i in state.keys():
        state[i] += 1
    else:
        state[i] = 1

iterations = 75

def transform(rock):
    if rock == '0':
        return ['1']
    if len(rock)%2 == 0:
        return [rock[:int(len(rock)/2)], str(int(rock[int(len(rock)/2):]))]
    else:
        return [str(int(rock)*2024)]

def iterate(state):
    newState = {}
    for i in state.keys():
        result = transform(i)
        for j in result:
            if j in newState.keys():
                newState[j] += state[i]
            else:
                newState[j] = state[i]
    return newState

for i in range(iterations):
    state = iterate(state)


print(sum(state.values()))