input = [int(i) for i in open(r'Day 9\test.txt', 'r').read()]

disk = []

memory = 0
#load memory
for i in range(0, len(input)):
    #block
    if i%2 == 0:
        disk += [memory for _ in range(input[i])]
        memory += 1
    #space
    else:
        disk += ['.' for _ in range(input[i])]

def rearrange(disk):
    front = 0
    back = len(disk)-1
    while front < back:
        if disk[front] != '.':
            front += 1
            continue
        if disk[back] != '.':
            disk[front] = disk[back]
            disk[back] = '.'
        back -= 1
    return disk

#rearrange
disk = rearrange(disk)

sum = 0
for i, value in enumerate(disk):
    if value == '.':
        continue
    sum += i * value

print(sum)