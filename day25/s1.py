import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    pk1, pk2 = [int(line) for line in f.read().strip().splitlines()]  # public keys

def find_loop_size(pk, sn=7):   # sn = subject number
    value = 1
    for i in count(1):
        value *= sn
        value %= 20201227
        if value == pk:
            return i


lp1 = find_loop_size(pk1)
lp2 = find_loop_size(pk2)

def transform(lp, sn):
    value = 1
    for i in range(lp):
        value *= sn
        value %= 20201227
    return value

e1 = transform(lp2, pk1)
e2 = transform(lp1, pk2)

assert e1 == e2

print(e1)
