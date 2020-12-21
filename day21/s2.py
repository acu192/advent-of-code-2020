import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count, permutations
from aocd import submit
#from dateutil.parser import parse
from math import factorial


def nPr(n, r):
    return int(factorial(n)/factorial(n-r))


with open('input', 'rt') as f:
    foods = []
    for line in f.read().strip().splitlines():
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split()
        allergens = allergens[:-1].split(', ')
        foods.append((ingredients, allergens))
    foods = sorted(foods, key=lambda f: nPr(len(f[0]), len(f[1])))

all_ingredients = set()
all_allergens = set()

for ingredients, allergens in foods:
    for a in allergens:
        all_allergens.add(a)
    for i in ingredients:
        all_ingredients.add(i)

might_be = defaultdict(set)

for a in all_allergens:
    might_be[a] = set(all_ingredients)
    for ingredients, allergens in foods:
        if a in allergens:
            might_be[a] &= set(ingredients)
    #print(a, might_be[a])

maybe = defaultdict(set)  # key=ingredient  values=allergens maybe in it

def search(assignments, reverse_assignments, index):
    if index == len(foods):
        for i, a in assignments.items():
            maybe[i].add(a)
        return True
    #print(index)
    ingredients, allergens = foods[index]
    found_solution = False
    for ingredients_perm in permutations(ingredients, r=len(allergens)):
        works = True
        for i, a in zip(ingredients_perm, allergens):
            if i not in might_be[a]:
                works = False
                break
            if i in assignments and assignments[i] != a:
                works = False
                break
            if a in reverse_assignments and reverse_assignments[a] != i:
                works = False
                break
        if not works:
            continue
        assignments_here = {}
        for i, a in zip(ingredients_perm, allergens):
            if i not in assignments:
                assignments_here[i] = a
                assignments[i] = a
                reverse_assignments[a] = i
        sub_found_solution = search(assignments, reverse_assignments, index+1)
        if sub_found_solution:
            found_solution = True
        for i, a in assignments_here.items():
            del assignments[i]
            del reverse_assignments[a]
    return found_solution

search({}, {}, 0)

#for i, a in maybe.items():
#    print(i, a)

canon = []

for i, a in maybe.items():
    assert len(a) == 1
    canon.append((list(a)[0], i))

canon = sorted(canon)

#print(canon)

canon = ','.join([i for a, i in canon])

print(canon)

