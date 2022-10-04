#!/usr/bin/env python3

"""Sudoku Solver

Solves a 9x9 sudoku puzzle

Usage: $ python3 sudoku.py
"""

### Functions ###


def print_sudoku(puzzle: list) -> None:
    """Sudoku table print function

    Args:
        puzzle (list): the sudoku puzzle
    """
    length = len(puzzle)
    br = int(length**0.5)
    for i, r in enumerate(puzzle):
        row = ""
        if i != 0 and i % br == 0:
            print("|".join(["---" * br] * br))
        for j, c in enumerate(puzzle[i]):
            if j != 0 and j % br == 0:
                row += "|"
            if c == 0:
                row += " _ "
            else:
                row += f" {c} "
        print(row)


def brute_solve(puzzle: list) -> bool:
    """Brute Force Solver

    Args:
        puzzle (list): the sudoku puzzle

    Returns:
        bool: the value True if the puzzle was solved
        else False if the puzzle does not have a valid
        solution
    """
    size = len(grid)
    if size and int(size**0.5) ** 2 == size and size == len(grid[0]):
        return brute_solve_helper(puzzle, 0, 0)
    else:
        print("[-] The puzzle is invalid. Reformat the puzzle and try again.")
        return False


def brute_solve_helper(grid: list, row: int, col: int) -> bool:
    """Recursive helper for brute_solve

    Args:
        grid (list): the sudoku puzzle
        row: the current row
        col: the current column

    Returns:
        bool: bool value for successful solve
    """
    size = len(grid)
    if row == size:
        return True
    if col == size:
        return True


def function(puzzle: list) -> None:
    """Sudoku table print function

    Args:
        puzzle (list): the sudoku puzzle

    Returns:
        type: _description_
    """
    return puzzle


if __name__ == "__main__":
    easy_puzzle = [
        [0, 0, 4, 0, 5, 0, 0, 0, 0],
        [9, 0, 0, 7, 3, 4, 6, 0, 0],
        [0, 0, 3, 0, 2, 1, 0, 4, 9],
        [0, 3, 5, 0, 9, 0, 4, 8, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0],
        [0, 7, 6, 0, 1, 0, 9, 2, 3],
        [3, 1, 0, 9, 7, 0, 2, 0, 0],
        [0, 0, 9, 1, 8, 2, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 1, 0, 0],
    ]
    medium_puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 1, 3],
        [8, 0, 0, 3, 0, 2, 5, 0, 0],
        [0, 0, 4, 0, 1, 0, 7, 0, 9],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [3, 4, 6, 0, 0, 0, 9, 7, 2],
        [0, 0, 8, 0, 0, 0, 0, 0, 6],
        [6, 0, 7, 0, 2, 0, 1, 0, 0],
        [0, 0, 5, 9, 0, 6, 0, 0, 7],
        [2, 9, 0, 0, 0, 0, 0, 0, 0],
    ]
    hard_puzzle = [
        [2, 0, 0, 5, 0, 7, 4, 0, 6],
        [0, 0, 0, 0, 3, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 3, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [8, 6, 0, 3, 1, 0, 0, 0, 0],
        [0, 4, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 7, 0, 0],
        [0, 0, 6, 9, 5, 0, 0, 0, 2],
        [0, 0, 1, 0, 0, 6, 0, 0, 8],
    ]
    print_sudoku(easy_puzzle)
