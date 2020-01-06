#!/usr/bin/env python3
'''
P2: Even Fibonacci Numbers
'''
def p2(maxN):
    i,j,s=1,2,2
    while j<maxN:
        i,j = j,i+j
        if not j%2: s += j
    return s

print('Below 4M:',p2(4000000)) # 4613732
