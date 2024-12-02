file = open(r'Day 2\input.txt', 'r')

def report_passes(report, remove):
    if remove > -1:
        report = report.copy()
        report.pop(remove)

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
        return 1
    return 0

total = 0

for report in file.readlines():
    report = [int(i) for i in report.split()]
    for i in range(-1, len(report)):
        if report_passes(report, i):
            total += 1 
            break
    
    
        


print(total)