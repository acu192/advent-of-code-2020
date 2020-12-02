import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse

stuff = []


with open('input', 'rt') as f:
    for line in f:
        a, p = line.split(': ')
        a, l = a.split(' ')
        i, j = a.split('-')
        i = int(i)
        j = int(j)
        stuff.append((i, j, l, p))


def part1(stuff):
    v = 0
    for i, j, l, p in stuff:
        c = Counter(p)
        c = c.get(l, 0)
        if i <= c and c <= j:
            v += 1
    print(v)
    #submit(v)


def part2(stuff):
    v = 0
    for i, j, l, p in stuff:
        i -= 1
        j -= 1
        if p[i] == l:
            if p[j] != l:
                v += 1
        else:
            if p[j] == l:
                v += 1
    print(v)
    #submit(v)


#part1(stuff)
part2(stuff)

