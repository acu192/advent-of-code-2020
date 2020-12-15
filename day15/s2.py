import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse


with open('input', 'rt') as f:
    nums = [int(v) for v in f.read().strip().split(',')]


said = {n: [i] for i, n in enumerate(nums)}

last = nums[-1]

i = len(nums)

while i < 30000000:
    prev_said = said[last]
    if len(prev_said) == 1:
        curr = 0
    else:
        curr = i - prev_said[-2] - 1
    last = curr
    if curr in said:
        said[curr].append(i)
    else:
        said[curr] = [i]
    i += 1


print(last)

