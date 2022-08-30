import sys
import numpy as np

if len(sys.argv) != 2:
    print(f'[!] Usage: python3 {sys.argv[0]} <file>')
    exit(1)

file = sys.argv[1]

li = [[i for i in x.replace('\n', '')] for x in open(file, 'r').readlines()]

### PROBLEM 1 ###

# vars

bits_1 = [0]*len(li[0])
bits_0 = [0]*len(li[0])

# logic

for bin_num in li:
    for i, bit in enumerate(bin_num):
        if bit == '1':
            bits_1[i] += 1
        else:
            bits_0[i] += 1

print(f'Bits 1: {bits_1}')
print(f'Bits 0: {bits_0}')

gamma = [1 if x > y else 0 for x,y in zip(bits_1, bits_0)]
epsilon = [1 if x > y else 0 for x,y in zip(bits_0, bits_1)]

gamma_dec = int(''.join(str(x) for x in gamma), 2)
epsilon_dec = int(''.join(str(x) for x in epsilon), 2)

print(f'Problem 1: Gamma = {gamma}, Epsilon = {epsilon}, Result = {gamma_dec * epsilon_dec}')

### PROBLEM 2 ###

def reduce_list(li, bit_idx, id):
    # id 1 for oxygen or id 0 for carbon dioxide
    cnt_1 = 0
    cnt_0 = 0

    for bin_num in li:
        if bin_num[bit_idx] == '1':
            cnt_1 += 1
        else:
            cnt_0 += 1

    comp = None
    temp = []

    if id == 1:
        if cnt_1 >= cnt_0:
            comp = '1'
        else:
            comp = '0'
    else:
        if cnt_0 <= cnt_1:
            comp = '0'
        else:
            comp = '1'

    for bin_num in li:
        if bin_num[bit_idx] == comp:
            temp.append(bin_num)

    return temp

length = len(li[0])
oxygen = li

for idx in range(length):
    oxygen = reduce_list(oxygen, idx, 1)
    if len(oxygen) == 1: break

oxygen = int(''.join(str(x) for x in oxygen[0]), 2)
print(f'Oxygen: {oxygen}')

carbon = li

for idx in range(length):
    carbon = reduce_list(carbon, idx, 0)
    if len(carbon) == 1: break

carbon = int(''.join(str(x) for x in carbon[0]), 2)
print(f'Carbon Dioxide: {carbon}')

print(f'Problem 2: {(oxygen)*(carbon)}')
