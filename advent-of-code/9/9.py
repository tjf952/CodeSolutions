import sys
from functools import reduce

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [[int(c) for c in x.replace('\n', '')] for x in open(file, 'r').readlines()]

### PROBLEM 1 ###

def calc_risk(grid):
    lowpoints = {}
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            curr = grid[i][j]
            left = grid[i][j-1] if j > 0 else 9
            right = grid[i][j+1] if j < cols-1 else 9
            up = grid[i-1][j] if i > 0 else 9
            down = grid[i+1][j] if i < rows-1 else 9
            if curr < left and curr < right and curr < down and curr < up:
                lowpoints[(i,j)] = grid[i][j]
    return lowpoints

lowpoints = calc_risk(li)
print(f'Problem 1: {sum(lowpoints.values()) + len(lowpoints)}')

### PROBLEM 2 ###
def check(grid, i, j):
    if i < 0 or i >= len(grid):
        return False
    if j < 0 or j >= len(grid[0]):
        return False
    if grid[i][j] == 9:
        return False
    return True

def bfs(grid, i, j):
    visited, queue = [], []
    visited.append((i,j))
    queue.append((i,j))
    while queue:
        i,j = queue.pop()
        for x,y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if check(grid, x, y) and (x,y) not in visited:
                visited.append((x,y))
                queue.append((x,y))
    return len(visited)

def calc_basin(grid, lowpoints):
    basins = []
    for (i,j), value in lowpoints.items():
        basins.append(bfs(grid, i, j))
    basins.sort(reverse=True)
    return reduce(lambda x,y: x*y, basins[:3]) 

print(f'Problem 2: {calc_basin(li, lowpoints)}')

