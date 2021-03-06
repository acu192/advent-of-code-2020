import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input_part2', 'rt') as f:
    rules, strs = f.read().strip().split('\n\n')
    rules = rules.splitlines()
    rules = {int(a): r for a, r in [rule.split(': ') for rule in rules]}
    strs = strs.splitlines()

def resolve(rules, index, depth):
    if depth > 500:
        return ''
    rule = rules[index]
    if rule.startswith('"'):
        return rule.replace('"', '')
    else:
        ors = rule.split(' | ')
        r_ors = []
        for o in ors:
            cats = []
            for a in o.split(' '):
                r = resolve(rules, int(a), depth+1)
                cats.append(r)
            r_ors.append(''.join(cats))
        group = '|'.join(r_ors)
        return '(' + group + ')'

sys.setrecursionlimit(2000)

re_equiv = resolve(rules, 0, 0)

#print(re_equiv)

matches = [s for s in strs if re.fullmatch(re_equiv, s)]

a = len(matches)

print(a)
#submit(a)

