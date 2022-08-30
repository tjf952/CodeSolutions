#!/usr/bin/env python3
'''
P3: Largest Prime Factor
'''
def p3(x):
    m = -1
    while not x%2: x/=2
    for i in range(3, int(x**.5)+1,2):
        while not x%i: m,x = i,x/i
    return m

print('Largest Prime Factor',p3(13195)) # 29
print('Largest Prime Factor:',p3(600851475143)) # 6857
