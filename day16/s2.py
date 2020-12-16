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


others.append(mine)


def get_maybes(v):
    m = set()
    for name, ranges in rules.items():
        for rng in ranges:
            if v >= rng[0] and v <= rng[1]:
                m.add(name)
    return m


others = [o for o in others if all([len(get_maybes(v)) > 0 for v in o])]


transposed = [[] for _ in mine]

for o in others:
    for i, v in enumerate(o):
        transposed[i].append(v)


can_be = [set(rules.keys()) for _ in mine]


def is_done():
    for c in can_be:
        if len(c) > 1:
            return False
    return True


solved = set()


while not is_done():
    for i, col in enumerate(transposed):
        for v in col:
            can_be[i] &= get_maybes(v)
        assert len(can_be[i]) > 0
        if len(can_be[i]) == 1 and i not in solved:
            solved.add(i)
            thisone = list(can_be[i])[0]
            for j, _ in enumerate(can_be):
                if j != i and thisone in can_be[j]:
                    can_be[j].remove(thisone)


m = 1

for i, s in enumerate(can_be):
    assert len(s) == 1
    thisone = list(s)[0]
    if thisone.startswith('departure'):
        m *= mine[i]


print(m)

