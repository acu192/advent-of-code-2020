import re, sys, os, string
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    passes = []
    vals = f.read().strip().split('\n\n')
    for val in vals:
        passes.append(val.split())


def part1(passes):
    c = 0

    needs = {
        'byr',  # (Birth Year)
        'iyr',  # (Issue Year)
        'eyr',  # (Expiration Year)
        'hgt',  # (Height)
        'hcl',  # (Hair Color)
        'ecl',  # (Eye Color)
        'pid',  # (Passport ID)
        #'cid',  # (Country ID)
    }

    for p in passes:
        has = set()
        for v in p:
            k, v = v.split(':')
            has.add(k)
        if len(needs - has) == 0:
            c += 1

    print(c)
    #submit(c)


def chk_byr(v):
    try:
        v = int(v)
        return v >= 1920 and v <= 2002
    except:
        return False

def chk_iyr(v):
    try:
        v = int(v)
        return v >= 2010 and v <= 2020
    except:
        return False

def chk_eyr(v):
    try:
        v = int(v)
        return v >= 2020 and v <= 2030
    except:
        return False

def chk_hgt(v):
    try:
        if v.endswith('in'):
            v = int(v[:-2])
            return v >= 59 and v <= 76
        elif v.endswith('cm'):
            v = int(v[:-2])
            return v >= 150 and v <= 193
        else:
            return False
    except:
        return False

def chk_hcl(v):
    valid = set(string.ascii_lowercase) | set('0123456789')
    if v.startswith('#'):
        if len(v) != 7:
            return False
        for c in v[1:]:
            if c not in valid:
                return False
        return True
    else:
        return False

def chk_ecl(v):
    valid = {
        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',
    }
    return v in valid

def chk_pid(v):
    valid = set('0123456789')
    if len(v) != 9:
        return False
    for c in v:
        if c not in valid:
            return False
    return True

def part2(passes):
    c = 0

    needs = {
        'byr': chk_byr,  # (Birth Year)
        'iyr': chk_iyr,  # (Issue Year)
        'eyr': chk_eyr,  # (Expiration Year)
        'hgt': chk_hgt,  # (Height)
        'hcl': chk_hcl,  # (Hair Color)
        'ecl': chk_ecl,  # (Eye Color)
        'pid': chk_pid,  # (Passport ID)
        #'cid': chk_cid,  # (Country ID)
    }

    for p in passes:
        has = set()
        for v in p:
            k, v = v.split(':')
            if k in needs and needs[k](v):
                has.add(k)
        if len(set(needs) - has) == 0:
            c += 1

    print(c)
    #submit(c)


#part1(passes)
part2(passes)

