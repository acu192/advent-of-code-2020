import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    s = f.read().strip()
    vals = [int(v) for v in re.findall('-?\d+', s)]


def part1(s):
    for a in vals:
        for b in vals:
            if a + b == 2020:
                o = a * b
    print(o)
    #submit(o)


def part2(s):
    for a in vals:
        for b in vals:
            for c in vals:
                if a + b + c == 2020:
                    o = a * b * c
    print(o)
    #submit(o)


part1(s)
part2(s)

