import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    lines = f.read().strip().splitlines()
    lines = [(v[0], int(v[1:])) for v in lines]

x, y = 0, 0   # +y=n, +x=e

d = 3   # 0=n, 1=w, 2=s, 3=e

right = {
    0: 3,
    1: 0,
    2: 1,
    3: 2,
}

left = {
    0: 1,
    1: 2,
    2: 3,
    3: 0,
}

for i, n in lines:
    if i == 'N':
        y += n
    elif i == 'S':
        y -= n
    elif i == 'E':
        x += n
    elif i == 'W':
        x -= n
    elif i == 'L':
        for _ in range(n // 90):
            d = left[d]
    elif i == 'R':
        for _ in range(n // 90):
            d = right[d]
    elif i == 'F':
        if d == 0:
            y += n
        elif d == 1:
            x -= n
        elif d == 2:
            y -= n
        elif d == 3:
            x += n
        else:
            assert False
    else:
        assert False

a = abs(x) + abs(y)

print(a)

