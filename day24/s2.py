import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse

def parsepath(line):
    path = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == 'e':
            path.append('e')
        elif c == 'w':
            path.append('w')
        elif c == 's':
            i += 1
            c = line[i]
            if c == 'e':
                path.append('se')
            elif c == 'w':
                path.append('sw')
            else:
                assert False
        elif c == 'n':
            i += 1
            c = line[i]
            if c == 'e':
                path.append('ne')
            elif c == 'w':
                path.append('nw')
            else:
                assert False
        else:
            assert False
        i += 1
    return path

with open('input', 'rt') as f:
    paths = [parsepath(line) for line in f.read().strip().splitlines()]

# This can be thought of as 2-d but the axes are not perpendicular!

def follow(path):
    x, y = 0, 0
    for p in path:
        if p == 'e':
            x += 1
        elif p == 'w':
            x -= 1
        elif p == 'se':
            y += 1
        elif p == 'sw':
            x -= 1
            y += 1
        elif p == 'ne':
            x += 1
            y -= 1
        elif p == 'nw':
            y -= 1
        else:
            assert False
    return x, y

ends = [follow(path) for path in paths]

black = set()
c = Counter(ends)

for (x, y), count in c.most_common():
    if (count % 2) == 1:
        black.add((x, y))

tiles = {}

ma = max([max(x, y) for x, y in ends])
mult = 200

for x in range(-ma - mult, ma + mult):
    for y in range(-ma - mult, ma + mult):
        tiles[(x, y)] = ((x, y) in black)

adj = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, 1),
    (1, -1),
]

def doit():
    needs_flip = []
    for (x, y), is_black in tiles.items():
        c = 0
        for dx, dy in adj:
            if tiles.get((x + dx, y + dy), False):
                c += 1
        if is_black:
            if c == 0 or c > 2:
                needs_flip.append((x, y))
        else:
            if c == 2:
                needs_flip.append((x, y))
    for x, y in needs_flip:
        tiles[(x, y)] = not tiles[(x, y)]


for _ in range(100):
    doit()

c = 0

for (x, y), is_black in tiles.items():
    if is_black:
        c += 1

print(c)

