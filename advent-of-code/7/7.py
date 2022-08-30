import sys
from collections import Counter
import time

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

crabs = [int(x) for x in open(file, 'r').read().split(',')]

### PROBLEM 1 ###

def get_minimum_change(crabs):
    min_pos, max_pos = min(crabs), max(crabs)
    min_result = float('inf')

    for i in range(min_pos, max_pos + 1):
        result = sum(abs(x-i) for x in crabs)
        if result < min_result:
            min_result = result

    return min_result


print(f'\nProblem 1: {get_minimum_change(crabs)}')

### PROBLEM 2 ###

def get_best_change(crabs):
    min_pos, max_pos = min(crabs), max(crabs)
    min_result = float('inf')

    for i in range(min_pos, max_pos + 1):
        result = sum(sum(range(abs(x-i)+1)) for x in crabs)
        # result = sum((1/2)*(abs(x-i) + abs(x-i)**2) for x in crabs)
        if result < min_result:
            min_result = result

    return min_result


print(f'\nProblem 2: {get_best_change(crabs)}')

# Part 1: 354564
# Part 2: 1609058859115
