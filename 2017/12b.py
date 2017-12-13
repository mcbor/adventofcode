#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    12b.py
    ~~~~~~
    Advent of Code 2017 - Day 12: Digital Plumber
    Part Two

    There are more programs than just the ones in the group containing program
    ID 0. The rest of them have no way of reaching that group, and still might
    have no way of reaching each other.

    A group is a collection of programs that can all communicate via pipes
    either directly or indirectly. The programs you identified just a moment
    ago are all part of the same group. Now, they would like you to determine
    the total number of groups.

    In the example above, there were 2 groups: one consisting of programs
    0,2,3,4,5,6, and the other consisting solely of program 1.

    How many groups are there in total?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from collections import defaultdict


def solve(pipes):
    """Return number of groups.

    :pipes: string of pipes separated by newlines.
    :return: number of program that contain program ID 0

    >>> solve('''0 <-> 2
    ... 1 <-> 1
    ... 2 <-> 0, 3, 4
    ... 3 <-> 2, 4
    ... 4 <-> 2, 3, 6
    ... 5 <-> 6
    ... 6 <-> 4, 5''')
    2
    """

    graph = defaultdict(set)

    for line in pipes.split('\n'):
        pid, _, *tail = line.split()
        graph[pid].update(n.strip(', ') for n in tail)

    nodes = set(graph)
    groups = []

    while nodes:
        node = nodes.pop()
        visited = set()
        stack = [node]

        while stack:
            v = stack.pop()
            visited.add(v)

            for u in graph[v]:
                if u not in visited:
                    stack.append(u)
        groups.append(visited)
        nodes -= visited

    return len(groups)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
