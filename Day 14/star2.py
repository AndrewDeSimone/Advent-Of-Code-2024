import re
import matplotlib.pyplot as plt
robots = open(r'Day 14/input.txt', 'r').readlines()
width = 101
height = 103
maxUnique = 0

for i in range(width * height):
    grid = [[0 for j in range(height)] for i in range(width)]
    positions = []
    for robot in robots:
        start = [int(i) for i in re.findall('-*\d+', robot)]
        position = [start[0] ,start[1]]
        velocity = [start[2], start[3]]
        position = [(position[0] + velocity[0] * i)%width, (position[1] + velocity[1] * i)%height]
        grid[position[0]][position[1]] += 1
        positions.append(position[0] + position[1] * 1j)
    if len(positions) == len(set(positions)):
        print(i)
        plt.imshow(grid)
        plt.show()
