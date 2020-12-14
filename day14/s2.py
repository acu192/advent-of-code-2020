import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    prog = []
    for line in f.read().strip().splitlines():
        if line.startswith('mask ='):
            prog.append(('mask', line.split(' = ')[1]))
        else:
            a, value = line.split(' = ')
            addr = a.split('[')[1].split(']')[0]
            addr = int(addr)
            value = int(value)
            prog.append((addr, value))


mem = {}
mask = None


def gen(mask, addr, i, res):
    if i == len(mask):
        res.append(''.join(addr))
        return
    if mask[i] == 'X':
        addr0 = list(addr)
        addr1 = list(addr)
        addr0[i] = '0'
        addr1[i] = '1'
        gen(mask, addr0, i+1, res)
        gen(mask, addr1, i+1, res)
    elif mask[i] == '0':
        gen(mask, addr, i+1, res)
    elif mask[i] == '1':
        addr1 = list(addr)
        addr1[i] = '1'
        gen(mask, addr1, i+1, res)


def write(addr, val):
    addr = bin(addr)[2:]
    addr = addr.zfill(len(mask))
    all_addrs = []
    gen(list(mask), list(addr), 0, all_addrs)
    for addr in all_addrs:
        mem[addr] = val


for addr, value in prog:
    if addr == 'mask':
        mask = value
    else:
        write(addr, value)


s = 0

for addr, value in mem.items():
    s += value


print(s)
