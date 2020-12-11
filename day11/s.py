import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    plane = f.read().strip().splitlines()


def adjacents(plane, i, j, needle):
    dirs = [
        (-1, 0),
        ( 1, 0),
        (0,  1),
        (0, -1),
        (-1, -1),
        ( 1,  1),
        (-1,  1),
        ( 1, -1),
    ]
    c = 0
    for di, dj in dirs:
        if i+di < 0 or i+di >= len(plane):
            continue
        if j+dj < 0 or j+dj >= len(plane[0]):
            continue
        if plane[i+di][j+dj] == needle:
            c += 1
    return c


def adjacents2(plane, i, j, needle):
    dirs = [
        (-1, 0),
        ( 1, 0),
        (0,  1),
        (0, -1),
        (-1, -1),
        ( 1,  1),
        (-1,  1),
        ( 1, -1),
    ]
    c = 0
    for di, dj in dirs:
        for m in count(1):
            if i+m*di < 0 or i+m*di >= len(plane):
                break
            if j+m*dj < 0 or j+m*dj >= len(plane[0]):
                break
            thing = plane[i+m*di][j+m*dj]
            if thing == needle:
                c += 1
                break
            elif thing == '.':
                continue
            else:
                break
    return c


def iterate(plane, adjacents_func=adjacents, movethresh=4):
    rows, cols = len(plane), len(plane[0])
    nplane = [[None for j in range(cols)] for i in range(rows)]
    for i, row in enumerate(plane):
        for j, seat in enumerate(row):
            a = adjacents_func(plane, i, j, '#')
            if seat == '.':
                nplane[i][j] = '.'
            elif seat == 'L':
                nplane[i][j] = '#' if a == 0 else 'L'
            elif seat == '#':
                nplane[i][j] = 'L' if a >= movethresh else '#'
            else:
                assert False
            #print(plane[i][j], i, j, a, nplane[i][j])
    return nplane


def countThings(plane, needle):
    c = 0
    for row in plane:
        for seat in row:
            if seat == needle:
                c += 1
    return c


def part1(plane):
    prev = plane

    while True:
        plane = iterate(plane)
        if plane == prev:
            break
        prev = plane
        #for row in prev:
        #    print(''.join(row))
        #print()

    a = countThings(plane, '#')

    print(a)
    #submit(a)


def part2(plane):
    prev = plane

    while True:
        plane = iterate(plane, adjacents2, movethresh=5)
        if plane == prev:
            break
        prev = plane
        #for row in prev:
        #    print(''.join(row))
        #print()

    a = countThings(plane, '#')

    print(a)
    #submit(a)


#part1(plane)
part2(plane)

