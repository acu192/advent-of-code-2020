import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    t, busses = f.read().strip().splitlines()
    t = int(t)
    busses = [int(b) if b != 'x' else None for b in busses.split(',')]

n = []   # next times  (time, buss_id)

for b in busses:
    if b is None:
        continue
    mult = (t // b) if (t % b) == 0 else (t // b) + 1
    next_time = mult * b
    n.append((next_time, b))

next_time, buss_id = min(n)

a = (next_time - t) * buss_id

print(a)
#submit(a)
