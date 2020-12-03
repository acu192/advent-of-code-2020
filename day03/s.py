import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    m = []
    for line in f:
        line = line.strip()
        if line:
            m.append(line)


def part1(m):
    t = 0
    y, x = 1, 3

    while y < len(m):
        if m[y][x % len(m[y])] == '#':
            t += 1
        y += 1
        x += 3

    print(t)
    #submit(t)


def part2(m):
    ts = 1

    for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        t = 0
        y, x = d, r

        while y < len(m):
            if m[y][x % len(m[y])] == '#':
                t += 1
            y += d
            x += r

        ts *= t

    print(ts)
    #submit(ts)


#part1(m)
part2(m)

