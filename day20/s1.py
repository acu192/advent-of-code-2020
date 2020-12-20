import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


def fix(tile):
    tile = tile.splitlines()
    id_ = int(tile[0][:-1].split()[1])
    tile = [list(line) for line in tile[1:]]
    return id_, tile

with open('input', 'rt') as f:
    tiles = f.read().strip().split('\n\n')
    tiles = [fix(tile) for tile in tiles]
    tiles = {id_: t for id_, t in tiles}
    grid_rows, grid_cols = 12, 12
    assert len(tiles) == grid_rows * grid_cols

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

def left_edge(tile):
    r, c = len(tile), len(tile[0])
    e = []
    for i in range(r):
        e.append(tile[i][0])
    return e

def right_edge(tile):
    r, c = len(tile), len(tile[0])
    e = []
    for i in range(r):
        e.append(tile[i][c-1])
    return e

def top_edge(tile):
    return tile[0]

def bottom_edge(tile):
    return tile[-1]

def find_fit(top, left, all_tiles, used_tile_ids):
    candidates = []
    for id_, tile in all_tiles.items():
        if id_ in used_tile_ids:
            continue
        for tile_transformed, did_flip, rotation in enumerate_tile(tile):
            if (top is None or top == top_edge(tile_transformed)) and (left is None or left == left_edge(tile_transformed)):
                candidates.append((id_, tile_transformed, did_flip, rotation))
    assert len(candidates) < 2
    if candidates:
        return candidates[0]

def tryit(start_id, all_tiles):
    start_tile = all_tiles[start_id]
    grid = [[None for _ in range(grid_cols)] for _ in range(grid_rows)]
    used_tile_ids = set()
    grid[0][0] = (start_id, start_tile, 0, 0)
    used_tile_ids.add(start_id)
    for j in range(1, grid_cols):
        needle = find_fit(None, right_edge(grid[0][j-1][1]), all_tiles, used_tile_ids)
        if needle is None:
            return False
        grid[0][j] = needle
        used_tile_ids.add(needle[0])
    for i in range(1, grid_rows):
        needle = find_fit(bottom_edge(grid[i-1][0][1]), None, all_tiles, used_tile_ids)
        if needle is None:
            return False
        grid[i][0] = needle
        used_tile_ids.add(needle[0])
        for j in range(1, grid_cols):
            needle = find_fit(bottom_edge(grid[i-1][j][1]), right_edge(grid[i][j-1][1]), all_tiles, used_tile_ids)
            if needle is None:
                return False
            grid[i][j] = needle
            used_tile_ids.add(needle[0])
    return grid

def run():
    for id_, tile in tiles.items():
        #print('trying:', id_)
        grid = tryit(id_, tiles)
        if grid is not False:
            tl_id = grid[0][0][0]
            tr_id = grid[0][grid_cols-1][0]
            bl_id = grid[grid_rows-1][0][0]
            br_id = grid[grid_rows-1][grid_cols-1][0]
            a = tl_id * tr_id * bl_id * br_id
            print('top-left tile id:', id_)
            print('part 1:', a)

            r, c = len(tile), len(tile[0])
            combined_picture = []

            for gr in range(grid_rows):
                for i in range(1, r-1):
                    row = []
                    for gc in range(grid_cols):
                        for j in range(1, c-1):
                            row.append(grid[gr][gc][1][i][j])
                    combined_picture.append(row)

            combined_picture = '\n'.join([''.join(row) for row in combined_picture])

            with open('input_part2', 'wt') as f:
                f.write(combined_picture)

run()

