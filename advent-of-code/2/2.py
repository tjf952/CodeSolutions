import sys

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [x.split() for x in open(file, 'r').readlines()]
m = {'up':-1, 'down':1}
x = y = 0

for d, v in li:
    v = int(v)
    if d == 'forward':
        x += v
    else:
        y += m[d]*v

print(f'Problem 1: Coord - ({x}, {y}), Result - {x*y}')

aim = x = y = 0

for d, v in li:
    v = int(v)
    if d == 'forward':
        x += v
        y += aim*v
    else:
        aim += m[d]*v

print(f'Problem 2: Coord - ({x}, {y}, {aim}), Result = {x*y}')

