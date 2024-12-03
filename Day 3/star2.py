import re

input = open(r"Day 3\input.txt", "r").read()
valid = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", input)

enabled = True

sum = 0

for i in valid:
    if(i == "don't()"):
        enabled = False
    elif(i == "do()"):
        enabled = True
    else:
        i = [int(j) for j in i[4:-1].split(",")]
        sum += (i[0] * i[1] * enabled)

print(sum)