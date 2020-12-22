import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    a, b = f.read().strip().split('\n\n')
    a = [int(i) for i in a.splitlines()[1:]]
    b = [int(i) for i in b.splitlines()[1:]]
    a = deque(a)
    b = deque(b)

while len(a) and len(b):
    x = a.popleft()
    y = b.popleft()

    assert x != y

    if x > y:
        a.append(x)
        a.append(y)
    else:
        b.append(y)
        b.append(x)

c = 0

w = a if len(a) else b

for i, v in enumerate(list(w)[::-1]):
    c += (i+1) * v

print(c)

