#!/usr/bin/env python3
# Advent of Code 2016 - Day 13, Part One & Two

import sys
from itertools import chain, combinations, product

# test set
# start = (1, 1)
# goal  = (7, 4)
# magic = 10

# part one & two
start = (1, 1)
goal  = (31, 39)
magic = 1352

def is_valid(coord):
    x, y = coord
    if x < 0 or y < 0:
        return False
    s = x*x + 3*x + 2*x*y + y + y*y + magic
    popcount = bin(s).count('1')
    return popcount % 2 == 0

def gen_moves(coord):
    x, y = coord
    moves = [(x+dx, y+dy) for dx, dy in [(0,-1), (1,0), (0,1), (-1, 0)]]
    return filter(is_valid, moves)     
        

def bfs_paths(start, goal, limit=None):
    iterations = 0
    queue = [(start, [start])]
    visited = set(start)
    while queue:
        (vertex, path) = queue.pop(0)
        for current in set(gen_moves(vertex)) - set(path):
            if limit and len(path) > limit:
                yield visited
                return
            iterations += 1
            if current == goal:
                yield path
            elif current in visited:
                continue
            else:
                visited.add(current)
                queue.append((current, path + [current]))
                
def shortest_path(start, goal, limit=None):
    try:
        return next(bfs_paths(start, goal, limit))
    except StopIteration:
        return None 

def main(argv):
    path = shortest_path(start, goal)
    print(len(path))
    visited = shortest_path(start, goal, 50)
    print(len(visited))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
