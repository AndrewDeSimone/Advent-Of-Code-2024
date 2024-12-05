def valid(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

input = [i.strip('\n') for i in open(r'Day 5\input.txt', 'r').readlines()]
rules, updates = (input[:input.index('')] , input[input.index('')+1:])

rules = [tuple([int(j) for j in i.split('|')]) for i in rules]
updates = [[int(j) for j in i.split(',')] for i in updates]

sum = 0

for update in updates:
    if valid(update, rules):
        sum += update[int(len(update)/2)]

print(sum)