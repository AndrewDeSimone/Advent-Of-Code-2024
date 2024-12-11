input = open(r'Day 11\input.txt', 'r').read().split()

iterations = 25

def iterate(row):
    newInput = []
    for i in row:
        if i == '0':
            newInput.append('1')
        elif len(i)%2==0:
            newInput.append(i[:int(len(i)/2)])
            newInput.append(str(int(i[int(len(i)/2):])))
        else:
            newInput.append(str(int(i)*2024))
    return newInput

for i in range(iterations):
    input = iterate(input)


print(len(input))