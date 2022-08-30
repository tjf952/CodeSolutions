#!/usr/bin/env python3
'''
P4: Largest Palindrome Product
'''
def p4(n):
    li = []
    for i in range(int('9'*n),int('1'+'0'*(n-1)),-1):
        for j in range(i,int('1'+'0'*(n-1)),-1):
            s = str(i*j)
            if s[:len(s)/2]==s[len(s)/2:][::-1]:
                li.append(int(s))
    return max(li)

print(p4(2))
print(p4(3))
