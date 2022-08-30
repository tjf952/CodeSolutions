import sys
from collections import deque

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [x.strip() for x in open(file, 'r').readlines()]
pairs = {'(':')', '[':']', '{':'}', '<':'>'}

### PROBLEM 1 ###

cost = {')':3, ']':57, '}':1197, '>':25137}

def syntax_error_finder(line):
    stack = deque()
    for c  in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        else:
            if c != pairs[stack.pop()]:
                return cost[c]
    return 0

total = 0

for line in li:
    total += syntax_error_finder(line)

print(f'\nProblem 1: {total}')

### PROBLEM 2 ###

complete_cost = {')':1, ']':2, '}':3, '>':4}

def syntax_completinator(line):
    stack = deque()
    valid = True
    for c  in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        else:
            if c != pairs[stack.pop()]:
                valid = False
                break
    if valid:
        sum_complete = 0
        for c in list(stack)[::-1]:
            sum_complete = sum_complete*5 + complete_cost[pairs[c]]
        return sum_complete
    return 0

ac = []

for line in li:
    value = syntax_completinator(line)
    if value: ac.append(value)

ac.sort()

print(f'\nProblem 2: {ac[len(ac)//2]}')

