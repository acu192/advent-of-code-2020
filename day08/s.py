import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


def inst(i):
    op, arg = i.split()
    return op, int(arg)


with open('input', 'rt') as f:
    prog = f.read().strip().splitlines()
    prog = [inst(i) for i in prog]


def go(prog):
    accum = 0
    execedlines = set()
    instpointer = 0

    while True:
        if instpointer >= len(prog):
            return True, accum
        op, arg = prog[instpointer]
        if instpointer in execedlines:
            return False, accum
        execedlines.add(instpointer)
        if op == 'nop':
            instpointer += 1
        elif op == 'acc':
            accum += arg
            instpointer += 1
        elif op == 'jmp':
            instpointer += arg
        else:
            assert False


def part1(prog):
    didterm, accum = go(prog)
    print(accum)
    #submit(accum)


def part2(prog):
    for i, (op, arg) in enumerate(prog):
        if op == 'nop':
            prop_copy = list(prog)
            prop_copy[i] = 'jmp', arg
            didterm, accum = go(prop_copy)
            if didterm:
                a = accum
                break
        elif op == 'jmp':
            prop_copy = list(prog)
            prop_copy[i] = 'nop', arg
            didterm, accum = go(prop_copy)
            if didterm:
                a = accum
                break

    print(a)
    #submit(a)


#part1(prog)
part2(prog)

