import sys

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [int(x) for x in open(file, 'r').readlines()]
up = 0
last = li[0] if len(li) else 0

for curr in li:
    if curr > last: up += 1
    last = curr

print(f'Problem 1: {up}')

up = 0
last = sum(li[:3]) if len(li) > 3 else sum(li[:len(li)])

for x,y,z in zip(li, li[1:], li[2:]):
    curr = x+y+z
    if curr > last: up += 1
    last = curr

print(f'Problem 2: {up}')

