import sys

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

puzzles = open(file, 'r').readlines()

"""
  0:6     1:2     2:5     3:5     4:4
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:5     6:6     7:3     8:7     9:6
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""

seg2num = {2:1, 4:4, 3:7, 7:8}
num2seg = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

### PROBLEM 1 ###

def find_key_values(puzzle):
    total = 0
    for combo in puzzle.split('|')[1].split():
        if len(combo) in seg2num.keys(): total += 1
    return total

total = 0

for puzzle in puzzles:
    total += find_key_values(puzzle)

print(f'Problem 1: {total}')

### PROBLEM 2 ###

def decode_puzzle(puzzle):
    decoder = {}
    keys = [set(combo) for combo in puzzle.split()]

    for combo in keys:
        key = len(combo)
        if key in seg2num.keys():
            decoder[seg2num[key]] = combo

    for key in [1,4,7,8]:
        keys.remove(decoder[key])

    for combo in keys:
        if len(combo ^ (decoder[7] | decoder[4])) == 1:
            decoder[9] = combo

    keys.remove(decoder[9])

    for combo in keys:
        if len(combo) == 6 and decoder[7].issubset(combo):
            decoder[0] = combo

    keys.remove(decoder[0])

    for combo in keys:
        if len(combo) == 6:
            decoder[6] = combo

    keys.remove(decoder[6])

    for combo in keys:
        if decoder[7].issubset(combo):
            decoder[3] = combo

    keys.remove(decoder[3])

    for combo in keys:
        if len(decoder[9] - combo) == 1:
            decoder[5] = combo

    keys.remove(decoder[5])
    decoder[2] = keys.pop()

    return decoder

sum_values = 0

for puzzle in puzzles:
    keys, puzzle = puzzle.split('|')
    decoder = decode_puzzle(keys)
    num = ''
    for combo in puzzle.split():
        combo = set(combo)
        for key, value in decoder.items():
            if combo == value:
                num += str(key)
    sum_values += int(num)

print(f'Problem 2: {sum_values}')
