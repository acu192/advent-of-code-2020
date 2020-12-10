import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    vals = [int(v) for v in f.read().strip().splitlines()]


def part1(vals):
    vals.extend([0, max(vals)+3])
    vals = sorted(vals)

    ones, threes = 0, 0

    for a, b in zip(vals[:-1], vals[1:]):
        diff = b - a
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

    a = ones * threes

    print(a)
    #submit(a)


def n(prev, i, vals, cache):
    if prev in cache:
        return cache[prev]
    if i >= len(vals):
        return 1
    s = 0
    while i < len(vals):
        val = vals[i]
        if val - prev <= 3:
            s += n(val, i+1, vals, cache)
        else:
            break
        i += 1
    cache[prev] = s
    return s


def part2(vals):
    vals.extend([max(vals)+3])
    vals = sorted(vals)

    cache = {}
    a = n(0, 0, vals, cache)

    print(a)
    #submit(a)


#part1(vals)
part2(vals)

