import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    plane = [list(line) for line in f.read().strip().splitlines()]
    # pretending we have a 50x50x50x50 space... we put the starting stuff aprox. in the middle
    space = {(x+25, y+25, 25, 25): v == '#' for x, line in enumerate(plane) for y, v in enumerate(line)}

def count(space, x, y, z, w):
    c = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    if space.get((x+dx, y+dy, z+dz, w+dw), False):
                        c += 1
    return c

def iterate(space):
    new_space = {}
    for x in range(50):
        for y in range(50):
            for z in range(50):
                for w in range(50):
                    c = count(space, x, y, z, w)
                    if space.get((x, y, z, w), False):
                        new_space[(x, y, z, w)] = c in (2, 3)
                    else:
                        new_space[(x, y, z, w)] = c == 3
    return new_space

for _ in range(6):
    space = iterate(space)

c = 0

for _, v in space.items():
    if v:
        c += 1

print(c)

