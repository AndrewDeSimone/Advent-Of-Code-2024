file = open(r'Day 2\input.txt', 'r')

total = 0

for report in file.readlines():
    report = [int(i) for i in report.split()]
    increase = report[0] < report[1]
    safe = True
    for i in range(len(report)-1):
        if increase:
            if report[i] > report[i+1]:
                safe = False
        else:
            if report[i] < report[i+1]:
                safe = False
        if abs(report[i] - report[i+1]) not in [1, 2, 3]:
            safe = False
    if safe:
        total+=1
        


print(total)