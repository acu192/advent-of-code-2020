import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    groups = f.read().strip().split('\n\n')


def part1(groups):
    c = 0

    for g in groups:
        s = set(g)
        if '\n' in s:
            s.remove('\n')
        c += len(s)

    print(c)
    #submit(c)


def part2(groups):
    c = 0

    for g in groups:
        s = set(g)
        if '\n' in s:
            s.remove('\n')
        for p in g.splitlines():
            s &= set(p)
        c += len(s)

    print(c)
    #submit(a)


#part1(groups)
part2(groups)

