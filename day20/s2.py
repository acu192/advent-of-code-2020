import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


MONSTER = """                  #
#    ##    ##    ###
 #  #  #  #  #  #
"""

monster_map = set()

for i, row in enumerate(MONSTER.splitlines()):
    for j, c in enumerate(row):
        if c == '#':
            monster_map.add((i, j))

with open('input_part2', 'rt') as f:
    pic = f.read().strip().splitlines()
    pic = [list(line) for line in pic]
    assert len(pic) == 96 and len(pic[0]) == 96

def rotate(tile):
    """rotates clockwise 90 degrees"""
    r, c = len(tile), len(tile[0])
    ntile = [[None for _ in range(r)] for _ in range(c)]
    for i, row in enumerate(tile):
        for j, v in enumerate(row):
            ntile[j][r-i-1] = v
    return ntile

def flip(tile):
    """flip left-to-right"""
    r, c = len(tile), len(tile[0])
    ntile = [[None for _ in range(c)] for _ in range(r)]
    for i, row in enumerate(tile):
        for j, v in enumerate(row):
            ntile[i][c-j-1] = v
    return ntile

def enumerate_tile(tile):
    for i in range(4):
        yield tile, 0, i
        tile = rotate(tile)
    tile = flip(tile)
    for i in range(4):
        yield tile, 1, i
        tile = rotate(tile)

def search_monsters(pic):
    is_monster = set()
    n = 0
    c = 0
    for i, row in enumerate(pic):
        for j, v in enumerate(row):
            if v == '#':
                c += 1
            for mi, mj in monster_map:
                if i+mi >= len(pic) or j+mj >= len(pic[0]):
                    break
                if pic[i+mi][j+mj] != '#':
                    break
            else:
                n += 1
                for mi, mj in monster_map:
                    is_monster.add((i+mi, j+mj))
    return n, (c - len(is_monster))

for t, _, _ in enumerate_tile(pic):
    n, c = search_monsters(t)
    if n > 0:
        print(c)

