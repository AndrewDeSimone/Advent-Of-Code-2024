import re
test = False
robots = open(r'Day 14/test.txt', 'r').readlines()
width = 11
height = 7
if not test:
    robots = open(r'Day 14/input.txt', 'r').readlines()
    width = 101
    height = 103

quadrants = [0, 0, 0, 0]
for robot in robots:
    start = [int(i) for i in re.findall('-*\d+', robot)]
    position = [start[0] ,start[1]]
    velocity = [start[2], start[3]]
    position = [(position[0] + velocity[0] * 100)%width, (position[1] + velocity[1] * 100)%height]
    if position[0] < width/2 - 0.5 and position[1] < height/2-0.5:
        quadrants[0] += 1
    if position[0] > width/2 - 0.5 and position[1] < height/2-0.5:
        quadrants[1] += 1
    if position[0] < width/2 - 0.5 and position[1] > height/2-0.5:
        quadrants[2] += 1
    if position[0] > width/2 - 0.5 and position[1] > height/2-0.5:
        quadrants[3] += 1
    
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])