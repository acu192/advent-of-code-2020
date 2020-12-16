import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    parts = f.read().strip().split('\n\n')
    assert len(parts) == 3
    rules = {}
    for line in parts[0].splitlines():
        name, vals = line.split(': ')
        vals = vals.split(' or ')
        vals = [(int(a), int(b)) for a, b in [v.split('-') for v in vals]]
        assert name not in rules
        rules[name] = vals
    mine = [int(v) for v in parts[1].splitlines()[1].split(',')]
    others = [[int(v) for v in line.split(',')] for line in parts[2].splitlines()[1:]]


def get_maybes(v):
    m = set()
    for name, ranges in rules.items():
        for rng in ranges:
            if v >= rng[0] and v <= rng[1]:
                m.add(name)
    return m


invalid = []

for o in others:
    for v in o:
        maybe = get_maybes(v)
        if len(maybe) == 0:
            invalid.append(v)

a = sum(invalid)


print(a)
#submit(a)

