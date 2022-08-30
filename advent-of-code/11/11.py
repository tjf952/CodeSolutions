import sys

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [[int(c) for c in x.strip()] for x in open(file, 'r').readlines()]

### PROBLEM 1 ###



### PROBLEM 2 ###

def check_big_flash(li):
    return all(True if val == 0 else False for row in li for val in row)

### MAIN ###

for x in li: print(x)

print(f'\nProblem 1: {-1}')
print(f'\nProblem 2: {-1}')

