import re
input = open(r'Day 13\input.txt','r').read().split('\n\n')

total = 0

def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

for machine in input:
    a = [int(i) for i in re.findall('\d+', machine.split('\n')[0])]
    b = [int(i) for i in re.findall('\d+', machine.split('\n')[1])]
    prize = [int(i) + 10000000000000 for i in re.findall('\d+', machine.split('\n')[2])]
    matrix = [[a[0], b[0]], [a[1], b[1]]]
    det = determinant(matrix)
    matrixx = [[prize[0], b[0]], [prize[1], b[1]]]
    detx = determinant(matrixx)
    matrixy = [[a[0], prize[0]], [a[1], prize[1]]]
    dety = determinant(matrixy)
    if detx % det != 0 or dety % det != 0:
        continue
    x = detx/det
    y = dety/det
    total += 3 * x + y

print(int(total))