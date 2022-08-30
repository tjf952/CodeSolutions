import sys
from collections import Counter

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = []
with open(file, 'r') as fp:
    line = fp.readline()
    while line:
        a, arrow, b = line.split()
        a, b = a.split(','), b.split(',')
        a = (int(a[0]), int(a[1]))
        b = (int(b[0]), int(b[1]))
        li.append([a, b])
        line = fp.readline()

def list_points(a, b):
    if a[0] == b[0]:
        small, big = min(a[1], b[1]), max(a[1], b[1])
        return [(a[0], x) for x in range(small, big+1)]
    elif a[1] == b[1]:
        small, big = min(a[0], b[0]), max(a[0], b[0])
        return [(x, a[1]) for x in range(small, big+1)]
    else:
        x_range, y_range = [], []
        if a[0] < b[0]:
            x_range = range(a[0], b[0]+1)
        else:
            x_range = range(a[0], b[0]-1, -1)
        if a[1] < b[1]:
            y_range = range(a[1], b[1]+1)
        else:
            y_range = range(a[1], b[1]-1, -1)
        return list(zip(x_range, y_range))
    return []

points = []
for a,b in li:
    line_points = list_points(a,b)
    points.extend(line_points)

occurrences = Counter(points)

result = 0
for item in occurrences:
    if occurrences[item] > 1: result += 1

print(f'Problem 2: {result}')

