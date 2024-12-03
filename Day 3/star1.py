import re

input = open(r"Day 3\input.txt", "r").read()
valid = re.findall("mul\(\d+,\d+\)", input)

sum = 0

for i in valid:
    i = [int(j) for j in i[4:-1].split(",")]
    sum += (i[0] * i[1])

print(sum)