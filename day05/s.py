import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    s = f.read().strip().splitlines()


def part1(s):
    vals = []

    for v in s:
        row = v[:7].replace('F', '0').replace('B', '1')
        sea = v[7:].replace('L', '0').replace('R', '1')
        row = int(row, 2)
        sea = int(sea, 2)
        id_ = row * 8 + sea
        vals.append(id_)

    a = max(vals)

    print(a)
    submit(a)



def part2(s):
    vals = []

    for v in s:
        row = v[:7].replace('F', '0').replace('B', '1')
        sea = v[7:].replace('L', '0').replace('R', '1')
        row = int(row, 2)
        sea = int(sea, 2)
        id_ = row * 8 + sea
        vals.append(id_)

    a = min(vals)
    vals = set(vals)

    aa = None

    for i in count(a+1):
        if i not in vals:
            aa = i
            break

    print(aa)
    #submit(aa)


#part1(s)
part2(s)

