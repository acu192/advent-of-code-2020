import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


# https://en.wikipedia.org/wiki/Shunting-yard_algorithm


with open('input', 'rt') as f:
    homework = f.read().strip().splitlines()
    # integers are all single digits!

precedence = {
    '+': 1,  # <-- this happens first
    '*': 2,  # <-- then this!
    '(': 3,
}

def sy(prob):
    prob = prob.replace(' ', '')
    args = []
    ops = []
    for c in prob:
        if c.isnumeric():
            args.append(int(c))
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops[-1] != '(':
                args.append(ops.pop())
            ops.pop()  # <-- pops the '('
        else:
            assert c in precedence
            while ops and precedence[ops[-1]] <= precedence[c]:
                args.append(ops.pop())
            ops.append(c)
    stack = args + ops[::-1]
    return stack

def evaluate(prob):
    stack = sy(prob)
    ev = []
    for c in stack:
        if isinstance(c, int):
            ev.append(c)
        else:
            if c == '+':
                b = ev.pop()
                a = ev.pop()
                c = a + b
                ev.append(c)
            elif c == '*':
                b = ev.pop()
                a = ev.pop()
                c = a * b
                ev.append(c)
            else:
                assert False, c
    assert len(ev) == 1
    return ev[0]

res = []

for prob in homework:
    a = evaluate(prob)
    res.append(a)

a = sum(res)

print(a)

