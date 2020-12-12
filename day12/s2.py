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

x, y = 0, 0      # ship position: +y=n, +x=e
wx, wy = 10, 1   # waypoint position

def rotate_left(x, y):
    return -y, x

for i, n in lines:
    if i == 'N':
        wy += n
    elif i == 'S':
        wy -= n
    elif i == 'E':
        wx += n
    elif i == 'W':
        wx -= n
    elif i == 'L':
        for _ in range(n // 90):
            wx, wy = rotate_left(wx, wy)
    elif i == 'R':
        for _ in range(n // 90):
            for __ in range(3):   # three rights equal one left
                wx, wy = rotate_left(wx, wy)
    elif i == 'F':
        x += n*wx
        y += n*wy
    else:
        assert False

a = abs(x) + abs(y)

print(a)

