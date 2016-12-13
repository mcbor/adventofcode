#!/usr/bin/env python3
# Advent of Code 2016 - Day 11, Part One

from pprint import pprint
import sys
from itertools import tee, filterfalse, chain, combinations


start = (1, frozenset(['SG', 'PG', 'SM', 'PM']),        # Floor 1
            frozenset(['TG', 'RG', 'CG', 'RM', 'CM']),  # Floor 2
            frozenset(['TM']),                          # Floor 3
            frozenset())                                # Floor 4

goal = (4, frozenset(),                                                               # Floor 1
           frozenset(),                                                               # Floor 2
           frozenset(),                                                               # Floor 3
           frozenset(['SG', 'PG', 'SM', 'PM', 'TG', 'RG', 'CG', 'RM', 'CM', 'TM']))   # Floor 4
           
           
start2 = (1, frozenset(['EG','EM','DG','DM','SG', 'PG', 'SM', 'PM']),        # Floor 1
            frozenset(['TG', 'RG', 'CG', 'RM', 'CM']),  # Floor 2
            frozenset(['TM']),                          # Floor 3
            frozenset())                                # Floor 4

goal2 = (4, frozenset(),                                                               # Floor 1
           frozenset(),                                                               # Floor 2
           frozenset(),                                                               # Floor 3
           frozenset(['EG','EM','DG','DM','SG', 'PG', 'SM', 'PM', 'TG', 'RG', 'CG', 'RM', 'CM', 'TM']))   # Floor 4

           
test_start = (1, frozenset(['HM', 'LM']),
                 frozenset(['HG']),
                 frozenset(['LG']),
                 frozenset())
                 
test_goal = (4, frozenset(),
                frozenset(),
                frozenset(),
                frozenset(['HG', 'HM', 'LG', 'LM']))
                
                
def state_string(state):
    out = []
    for i in range(1,5):
        out.append('F' + str(i) + ': ')
        if state[0] == i:
            out.append('E ')
        for e in state[i]:
            out.append(e + ' ')
        out.append('\n')
    return "".join(out)


def partition(pred, iterable):
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def is_valid(state):
    if state[0] > 4 or state[0] < 1:
        return False
    for floor in state[1:]:
        generators, microchips = partition(lambda x: x[1] == 'M', floor)
        generators = set([g[0] for g in generators])
        microchips = set([m[0] for m in microchips])
        if len(generators) == 0 or len(microchips) == 0:
            # only generators or microchips on this floor
            continue
        if not microchips.issubset(generators):
            # some microchips don't have a corresponding generator, so they're fried
            return False
    return True


def gen_states(state, next):
    current = state[0]
    if next > 4 or next < 1:
        return
    moves = chain.from_iterable(combinations(state[current], r) for r in range(1, 3))
    for move in moves:
        new_state = list(state)
        new_state[0] = next
        new_state[current] -= set(move)
        new_state[next] |= set(move)
        if is_valid(new_state):
            yield tuple(new_state)


def next_states(state):
    states = chain(gen_states(state, state[0] + 1), gen_states(state, state[0] - 1)) 
    return set(states)

def bfs_paths(start, goal):
    iterations = 0
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        for next in next_states(vertex) - set(path):
            iterations += 1
            sys.stderr.write('{} {}\r'.format(iterations, len(path)))
            if next == goal:
                sys.stderr.write('\n')
                yield path + [next]
            elif next in visited:
                continue
            else:
                visited.add(next)
                queue.append((next, path + [next]))
                
def shortest_path(start, goal):
    try:
        return next(bfs_paths(start, goal))
    except StopIteration:
        return None 

def main(argv):
    path = shortest_path(start, goal)
    for step, state in enumerate(path):
        print('Step', step )
        print(state_string(state))
    print(len(path) - 1)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
