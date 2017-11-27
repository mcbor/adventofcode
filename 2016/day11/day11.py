#!/usr/bin/env python3
# Advent of Code 2016 - Day 11, Part One & Two

import sys
from itertools import chain, combinations

# test set
# start = (1, ((2,1), (3,1)))
# goal  = (4, tuple((4,4) for _ in range(len(start[1]))))

# part one
# start = (1, ((1,1), (1,1), (2,3), (2,2), (2,2)))
# goal  = (4, tuple((4,4) for _ in range(len(start[1]))))

# part two
start = (1, ((1,1), (1,1), (2,3), (2,2), (2,2), (1,1), (1, 1)))
goal  = (4, tuple((4,4) for _ in range(len(start[1]))))

def tuple2list(state):
    return [state[0], [list(i) for i in state[1]]]
    
def list2tuple(state):
    return (state[0], tuple(tuple(i) for i in state[1]))

def skey(state):
    return (state[0], tuple(sorted(state[1])))
    
def flatten(state):
    return [state[0]] + list(chain.from_iterable(state[1]))

def is_valid(state):
    if any(filter(lambda x: x < 1 or x > 4, flatten(state))):
        return False
    generators, microchips = zip(*state[1])
    for i, microchip in enumerate(microchips):
        if generators[i] != microchip and microchip in generators:
            return False
    return True

def gen_states(state):
    current_floor = state[0]

    # candidates will be 2-tuple values, with (pair, kind), 
    # whereby kind is 0 for the generator and 1 for the microchip
    candidates = []
    for kind, items in enumerate(zip(*state[1])):
        candidates += [(pair, kind) for pair, floor in enumerate(items) if floor == current_floor]
    combo = list(chain.from_iterable(combinations(candidates, r) for r in range(1, 3)))
    for delta in [-1, 1]:
        new_floor = current_floor + delta
        if new_floor < 1 or new_floor > 4:
            continue
        for c in combo:
            items = tuple2list(state)[1]
            for move in c:
                items[move[0]][move[1]] += delta
            if is_valid([new_floor, items]):
                yield list2tuple([new_floor, items])
        

def bfs_paths(start, goal):
    iterations = 0
    queue = [(start, [start])]
    visited = set(skey(start))
    while queue:
        (vertex, path) = queue.pop(0)
        for current in set(gen_states(vertex)) - set(path):
            iterations += 1
            sys.stderr.write('{} {}\r'.format(iterations, len(path)))
            if current == goal:
                sys.stderr.write('\n')
                yield path + [current]
            elif skey(current) in visited:
                continue
            else:
                visited.add(skey(current))
                queue.append((current, path + [current]))
                
def shortest_path(start, goal):
    try:
        return next(bfs_paths(start, goal))
    except StopIteration:
        return None 

def main(argv):
    path = shortest_path(start, goal)
    print(len(path) - 1)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
