import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from aocd import submit
#from dateutil.parser import parse


def normalize(b):
    if b.endswith(' bags'):
        return b[:-5]
    elif b.endswith(' bag'):
        return b[:-4]
    assert False


def parse_dependency(b):
    q, b = b.split(' ', maxsplit=1)
    return int(q), normalize(b)


with open('input', 'rt') as f:
    lines = f.readlines()
    graph = {}
    for line in lines:
        line = line.strip()[:-1]  # remove newline and period at end of line
        a, b = line.split(' contain ')
        b = b.split(', ')
        b = [v for v in b if v != 'no other bags']
        b = [parse_dependency(v) for v in b]
        a = normalize(a)
        #print([a, b])
        assert a not in graph
        graph[a] = b


def can_find(graph, curr, target, cache):
    if curr in cache:
        return cache[curr]
    if curr == target:
        return True
    found = False
    for _, nxt in graph[curr]:
        if can_find(graph, nxt, target, cache):
            found = True
            break
    cache[curr] = found
    return found


def part1(graph):
    c = 0

    target = 'shiny gold'

    for node in graph:
        if node == target:
            continue  # the target cannot be the outermost bag
        cache = {}
        yes = can_find(graph, node, target, cache)
        if yes:
            c += 1

    print(c)
    #submit(c)


def count(graph, curr, cache):
    if curr in cache:
        return cache[curr]
    c = 1
    for q, nxt in graph[curr]:
        c += q * count(graph, nxt, cache)
    cache[curr] = c
    return c


def part2(graph):
    target = 'shiny gold'
    cache = {}
    a = count(graph, target, cache) - 1
    print(a)
    #submit(a)


#part1(graph)
part2(graph)

