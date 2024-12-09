input = [int(i) for i in open(r'Day 9\input.txt', 'r').read()]

disk = []
memory = 0
#load memory
for i in range(0, len(input)):
    #block
    if i%2 == 0:
        disk.append((memory, input[i]))
        memory += 1
    #space
    else:
        disk.append((None, input[i]))

#rearrange
back = len(disk)-1
front = 0
while back >= 0:
    #no swap available
    if disk[back][0] == None or front >= back:
        front = 0
        back -= 1
        continue
    #swappable
    if disk[front][0] == None and disk[back][1] <= disk[front][1]:
        difference = disk[front][1] - disk[back][1]
        disk[front] = disk[back]
        disk[back] = (None, disk[back][1])
        if difference>0:
            disk.insert(front + 1, (None, difference))
        continue
    #not swappable
    front += 1

#tuple list to regular list
regList = []
for i in disk:
    if i[0] == None:
        regList += ['.' for j in range(0, i[1])]
        continue
    regList += [i[0] for j in range(0, i[1])]

sum = 0
for i, value in enumerate(regList):
    if value == '.':
        continue
    sum += i * value

print(sum)