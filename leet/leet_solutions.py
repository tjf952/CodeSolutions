#!/usr/bin/env python3

"""Leet Code Solutions

Daily solves for leet code

Usage: $ python3 leet_solutions.py
"""

### Import Statements ###

from collections import deque
from termcolor import colored, cprint

import math

### Helpers ###


def success(s):
    cprint(s, "green", attrs=["bold"])


def fail(s):
    cprint(s, "red", attrs=["bold", "reverse", "blink"])


### Functions ###


def dutch_sort(nums: list) -> list:
    """L75

    Args:
        nums (list): Array of integers with values 0, 1, and 2

    Returns:
        list: Sorted array
    """
    zero = 0
    one = 0
    two = len(nums)-1
    while one <= two:
        if nums[two] == 2:
            two -= 1
        elif nums[two] == 1:
            nums[two] = nums[one]
            nums[one] = 1
            one += 1
        else:
            nums[two] = nums[zero]
            nums[zero] = 0
            if zero == one:
                one += 1
            zero += 1
    return nums


def binary_search(nums: list, target: int) -> int:
    """L704

    Args:
        nums (list): Array of intergers sorted in ascending order
        target (int): An interger to find

    Returns:
        int: Index of target integer
    """
    b, e = 0, len(nums) - 1
    while e >= b:
        m = (b + e) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            b = m + 1
        else:
            e = m - 1
    return -1


def num_rescue_boats(people: list, limit: int) -> int:
    """L881

    Args:
        people (list): An array of people where people[i] is the weight of ith person
        limit (int): The maxmimum weight a boat can carry

    Returns:
        Minimum number of boats to carry every given person
    """
    boats = 0
    people = deque(sorted(people))
    while people:
        if people[-1] + people[0] <= limit:
            people.popleft()
        people.pop()
        boats += 1
    return boats


def min_cost_tickets(days: list, costs: list) -> int:
    """L983

    Args:
        days (list): A list of integers representing days of a year
        costs (list): 3 different types off tickets for 1, 7, and 30 day passes

    Returns:
        int: Minimum cost you need to travel every day in given list of days
    """
    last = days[-1]
    cal = [0] * (last + 1)
    days = set(days)
    for i in range(1, len(cal)):
        if i in days:
            cal[i] = cal[i - 1] + costs[0]
            cal[i] = min(cal[max(0, i - 7)] + costs[1], cal[i])
            cal[i] = min(cal[max(0, i - 30)] + costs[2], cal[i])
        else:
            cal[i] = cal[i - 1]
    return cal[last]


def successful_pairs(spells: list, potions: list, success: int) -> list:
    """L2300
    Uses binary search (binsearch) to do a logn search on potions

    Args:
        spells (list): List of integers representing strength of ith spell
        potions (list): List of integers representing strength of jth potion

    Returns:
        int: Minimum cost you need to travel every day in given list of days
    """

    def binsearchmax(nums, target):
        b, e = 0, len(nums) - 1
        while b <= e:
            m = b + (e-b) // 2
            if nums[m] >= target:
                e = m - 1
            else:
                b = m + 1
        return b

    potions.sort()
    for i in range(len(spells)):
        """
        spell[i] * potion[j] >= success
        potion[j] >= success/spell[i]
        find ceil(success/spell[i]) = idx --> len(potions[idx:]) = answer
        """
        idx = math.ceil(success / spells[i])
        idx = binsearchmax(potions, idx)
        spells[i] = len(potions) - idx
    return spells


def test(output, expected) -> bool:
    """Simple Test Function

    Args:
        output (template): Output of given function
        expected (template): Expected answer

    Returns:
        bool: Pass or fail based on assertion
    """
    if output == expected:
        success(f"[+] Output {output} is correct.")
        return True
    fail(f"[!] Incorrect!\n    Output: {output}\n  Expected: {expected}")
    return False


if __name__ == "__main__":
    print("TEST CASES")
    test(dutch_sort([1]), [1])
    test(dutch_sort([]), [])
    test(dutch_sort([2,1,0,1,2,0,1,0,2]), [0,0,0,1,1,1,2,2,2])