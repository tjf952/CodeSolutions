import sys
from collections import Counter
import time

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

fish = [int(x) for x in open(file, 'r').read().split(',')]

### PROBLEM 1 ###

def simple_count(fish, limit):
    days = 0

    while days < limit:
        new_fish = []

        for i in range(len(fish)):
            fish[i] = fish[i]-1
            if fish[i] == -1:
                fish[i] = 6
                new_fish.append(8)

        fish.extend(new_fish)
        days += 1

    return len(fish)

problem_1 = fish.copy()
start = time.time()
print(f'\nProblem 1: {simple_count(problem_1, 80)}')
end = time.time()
print(f'Runtime (brute): {end-start}s')

### PROBLEM 2 ###

def smart_count(fish, limit):
    fish = Counter(fish)
    for _ in range(limit):
        new_fish = Counter()
        for i in range(8):
            new_fish[i] = fish[i+1]
        new_fish[6] += fish[0]
        new_fish[8] = fish[0]
        fish = new_fish
    return sum(fish.values())

problem_2 = fish.copy()
start = time.time()
print(f'\nProblem 2: {smart_count(problem_2, 256)}')
end = time.time()
print(f'Runtime (dp): {end-start}s')

# Part 1: 354564
# Part 2: 1609058859115
