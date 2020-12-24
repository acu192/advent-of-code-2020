import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count


# Super-simple linked list: have an array `c` and set it up as `c[cup] = next_cup`
# Or, just to avoid a few initialization annoyances, use a map instead of an array.


with open('input', 'rt') as f:
    c = [int(v) for v in f.read().strip()]
    assert min(c) == 1
    cm = {}
    for i in range(len(c)-1):
        cm[c[i]] = c[i+1]
    cm[c[-1]] = c[0]
    mi, ma = min(c), max(c)
    first_cup = c[0]
    del c
    assert mi == 1
    assert ma == 9

def doit(curr_cup):
    last_pickup = curr_cup
    pickedup = []
    for i in range(3):
        last_pickup = cm[last_pickup]
        pickedup.append(last_pickup)
    after_pickup = cm[last_pickup]
    first_pickup = cm[curr_cup]
    cm[curr_cup] = after_pickup
    dest = curr_cup - 1
    while True:
        if dest < mi:
            dest = ma
        if dest not in pickedup:
            break
        dest -= 1
    cm[last_pickup] = cm[dest]
    cm[dest] = first_pickup
    return after_pickup

curr_cup = first_cup

for i in range(100):
    curr_cup = doit(curr_cup)

c = []
curr_cup = 1

while True:
    curr_cup = cm[curr_cup]
    if curr_cup != 1:
        c.append(curr_cup)
    else:
        break

print(''.join([str(v) for v in c]))

