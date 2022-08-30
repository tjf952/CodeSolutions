import sys
from collections import deque

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [x.strip().split('-') for x in open(file, 'r').readlines()]

### PROBLEM 1 ###

def make_neighbor_list(li):
    neighbors = {}
    for start, finish in li:
        if start in neighbors:
            neighbors[start].append(finish)
        else:
            neighbors[start] = [finish]
        if finish in neighbors:
            neighbors[finish].append(start)
        else:
            neighbors[finish] = [start]
    return neighbors

def find_paths(map):
    visited, queue = deque(['start']), deque(['start'])



neighbors = make_neighbor_list(li)
path_count = find_paths
print(f'\nProblem 1: {path_count}')

### PROBLEM 2 ###



print(f'\nProblem 2: {-1}')

