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

c = Counter(ends)

answer = 0

for (x, y), count in c.most_common():
    if (count % 2) == 1:
        answer += 1

print(answer)
