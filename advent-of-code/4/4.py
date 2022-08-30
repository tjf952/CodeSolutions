import sys

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

fp = open(file, 'r')
boards = []
nums = fp.readline().replace('\n', '').split(',')

while fp.readline():
    board = [fp.readline().split() for x in range(5)]
    boards.append(board)

### PROBLEM 1 ###

def check_winner(board):
    for row in board:
        if row == ['-1']*5:
            return True
    rotate = [list(x) for x in list(zip(*board[::-1]))]
    for col in rotate:
        if col == ['-1']*5:
            return True
    return False

def solve_board(board, choice):
    s = 0
    for row in board:
        for x in row:
            if int(x) >= 0:
                s += int(x)
    return s * int(choice)

def bingo(nums, boards):
    final = -1    

    for choice in nums:
        for board in range(len(boards)):
            for i in range(5):
                for j in range(5):
                    if boards[board][i][j] == choice:
                        boards[board][i][j] = '-1'
            win = check_winner(boards[board])
            if win:
                final = solve_board(boards[board], choice)
                return final

    return -1

final = bingo(nums, boards)

print(f'\nProblem 1: {final}\n')

### PROBLEM 2 ###

def bingo_last(nums, boards):
    final = -1
    remove_list = []

    for choice in nums:
        remove_list = []
        for board in range(len(boards)):
            for i in range(5):
                for j in range(5):
                    if boards[board][i][j] == choice:
                        boards[board][i][j] = '-1'
            win = check_winner(boards[board])
            if win:
                if len(boards) == 1:
                    final = solve_board(boards[board], choice)
                    return final
                else:
                    remove_list.append(boards[board])
        boards = [x for x in boards if x not in remove_list]

    return -1  

final2 = bingo_last(nums, boards)

print(f'\nProblem 2: {final2}\n')

