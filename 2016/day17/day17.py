#!/usr/bin/env python3
# Advent of Code 2016 - Day 17

import sys
from hashlib import md5
from itertools import compress, tee

start = (1, 1)
goal  = (4, 4)
passcode = 'veumntbg'
# test
# passcode = 'ihgpwlah' # DDRRRD
# passcode = 'kglvqrro' # DDUDRLRRUDRD
# passcode = 'ulqzkmiv' # DRURDRUDDLLDLUURRDULRLDUUDDDRR

dirs = {( 0, -1): 'U',
        ( 0,  1): 'D',
        (-1,  0): 'L',
        ( 1,  0): 'R' }
             
def directions(path):
    return ''.join([dirs[(n[0] - c[0], n[1] - c[1])] for c, n in pairwise(path)])

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def gen_moves(coord, path):
    x, y = coord

    moves = [(x+dx, y+dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]]
    valid = [0 < x < 5 and 0 < y < 5 for x, y in moves]
    
    digest = md5((passcode + directions(path)).encode('utf-8')).hexdigest()
    doors = [direction in 'bcdef' and valid[i] for i, direction in enumerate(digest[:4])]
    
    return compress(moves, doors)
        

def bfs_paths(start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for current in set(gen_moves(vertex, path)):
            if current == goal:
                yield path + [current]
            else:
                queue.append((current, path + [current]))
                
def shortest_path(start, goal):
    try:
        return next(bfs_paths(start, goal))
    except StopIteration:
        return None 

def main(argv):
    paths = bfs_paths(start, goal)
    paths = sorted(paths, key=lambda i: len(i))
    print(len(paths[0]) - 1)
    print(directions(paths[0]))
    print(len(paths[-1]) - 1)
    print(directions(paths[-1]))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
