import re, sys, os, math, functools
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    _, buses = f.read().strip().splitlines()
    buses = [int(b) if b != 'x' else None for b in buses.split(',')]
    buses = [(b, r) for r, b in enumerate(buses) if b is not None]
    buses = [(b, r % b) for b, r in buses]         # some remainders need to be further simplified
    buses = [(b, (b - r) % b) for b, r in buses]   # since we want the time t *before* the bus next arrival


print('find t...\n')

for b, r in buses:
    print('t = {} (mod {})'.format(r, b))

print()


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


lcm_curr = lcm(buses[0][0], buses[1][0])

for i in range(lcm_curr):
    if i % buses[0][0] == buses[0][1] and i % buses[1][0] == buses[1][1]:
        print('first two:', i)
        answer = i

"""
Here's the idea:

Above, we calculated the answer if there was only two buses. We don't search past `lcm_curr`
because the remainder pattern repeats after this the LCM of the first two buses.

Now, to figure out the next (third) bus, consider this:
    1. We save `lcm_curr` into `lcm_last` and use it as the step size (remember, the remainder pattern when dividing the first two buses repeats with a cycle of `lcm_last`)
    2. We compute a new LCM of the first *three* buses (now becomes `lcm_curr`) and we search up to it for a value that accommodates this new bus (we trust the offset/step-size ensures that the first two buses are still accommodated, thus they don't need to be re-checked).

This extends to the other buses in the same way...
"""

for b in buses[2:]:
    lcm_last = lcm_curr
    lcm_curr = lcm(lcm_curr, b[0])

    for i in range(answer, lcm_curr+1, lcm_last):
        if i % b[0] == b[1]:
            print('next', i)
            answer = i

print()
print('final answer:', answer)

