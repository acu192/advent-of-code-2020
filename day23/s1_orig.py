import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    c = [int(v) for v in f.read().strip()]

def doit(c, curr_index):
    print(c)
    mi, ma = min(c), max(c)
    curr = c[curr_index]
    orig_curr = curr
    l = len(c)
    picked = []
    for i in range(1, 4):
        picked.append(c[(curr_index+i)%l])
    print(picked)
    c = [c[(curr_index+i)%l] for i in range(4, 4+l-3)]
    print(c)
    while True:
        curr -= 1
        if curr < mi:
            curr = ma
        if curr in c:
            curr_index = c.index(curr)
            break
    print(curr_index, c[curr_index])
    for i in range(curr_index+1, curr_index+1+l-3):
        picked.append(c[i%(l-3)])
    print(picked)
    print()
    curr_index = picked.index(orig_curr)
    return picked, (curr_index+1)%l


curr_index = 0

for _ in range(100):
    c, curr_index = doit(c, curr_index)

l = len(c)

curr_index = (c.index(1) + 1) % l

answer = ''.join([str(c[(curr_index+i)%l]) for i in range(l-1)])
print(answer)

