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

def play(a, b):
    #print('== NEW GAME ==')

    a = deque(a)
    b = deque(b)

    cache = set()

    while len(a) and len(b):
        #print('p1:', a)
        #print('p2:', b)

        key = tuple(a) + ('/',) + tuple(b)
        if key in cache:
            #print('... seen this before ... p1 wins')
            return True, a
        cache.add(key)

        x = a.popleft()
        y = b.popleft()
        assert x != y

        if len(a) >= x and len(b) >= y:
            a_wins, _ = play(list(a)[0:x], list(b)[0:y])
            if a_wins:
                #print('p1 wins')
                a.append(x)
                a.append(y)
            else:
                #print('p2 wins')
                b.append(y)
                b.append(x)

        else:
            if x > y:
                #print('p1 wins')
                a.append(x)
                a.append(y)
            else:
                #print('p2 wins')
                b.append(y)
                b.append(x)

    #print('END OF GAME:' 'p1 wins' if a else 'p2 wins')
    #print()

    if a:
        # a wins
        return True, a
    else:
        # b wins
        return False, b

_, w = play(a, b)

c = 0

for i, v in enumerate(list(w)[::-1]):
    c += (i+1) * v

print(c)

