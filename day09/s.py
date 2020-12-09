import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    vals = [int(v) for v in f.readlines()]


def valid(vals, val):
    for i, a in enumerate(vals):
        for b in vals[i+1:]:
            if a + b == val:
                return True
    return False


def part1(vals):
    for i, v in enumerate(vals[25:]):
        prev = vals[i:i+25]
        if not valid(prev, v):
            break

    #print(v)
    #submit(v)
    return v


def part2(vals, needle):
    for i, a in enumerate(vals):
        s = a
        for j, b in enumerate(vals[i+1:], i+1):
            s += b
            if s == needle:
                subvals = vals[i:j+1]
                min_, max_ = min(subvals), max(subvals)

    ans = min_ + max_

    print(ans)
    #submit(ans)


needle = part1(vals)
part2(vals, needle)

