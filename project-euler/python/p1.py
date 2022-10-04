#!/usr/bin/env python3
"""
P1: Multiples of 3 and 5
"""


def p1(maxN):
    return sum(x for x in range(maxN) if not x % 3 or not x % 5)


print("Max is 10:", p1(10))  # 23
print("Max is 1000:", p1(1000))  # 233168
