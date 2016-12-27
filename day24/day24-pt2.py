#!/usr/bin/env python3
# Advent of Code 2016 - Day 24, Part One

import sys
from itertools import compress, combinations, permutations, chain, tee
from pprint import pprint

hvac = {}
locations = {}

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def gen_moves(vertex):
    x, y = vertex
    
    moves = [(x+dx, y+dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]]
    valid = [move in hvac and hvac[move] != '#' for move in moves]
    
    return compress(moves, valid)

def bfs_paths(start, goal):
    queue = [(start, [start])]
    visited = set(start)
    while queue:
        (vertex, path) = queue.pop(0)
        for current in set(gen_moves(vertex)) - set(path):
            if current == goal:
                yield path + [current]
            elif current in visited:
                continue
            else:
                visited.add(current)
                queue.append((current, path + [current]))
                
def shortest_path(start, goal):
    try:
        return next(bfs_paths(start, goal))
    except StopIteration:
        return None


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    with open(argv[1]) as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                hvac[(x, y)] = c
                if c.isdigit():
                    locations[int(c)] = (x, y)
        paths = {}
        for start, goal in combinations(locations, 2):
            paths[(start, goal)] = len(shortest_path(locations[start], locations[goal])) - 1
            paths[(goal, start)] = paths[(start, goal)]
        steps = 99999
        for p in permutations(range(1, max(locations.keys()) + 1)):
            steps = min(steps, sum(paths[(a, b)] for a, b in pairwise(chain([0], p, [0]))))
        print(steps)
    return 0
            

if __name__ == '__main__':
    sys.exit(main(sys.argv))
