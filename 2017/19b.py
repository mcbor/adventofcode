#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    19b.py
    ~~~~~~
    Advent of Code 2017 - Day 19: A Series of Tubes
    Part Two

    The packet is curious how many steps it needs to go.

    For example, using the same routing diagram from the example above...

         |
         |  +--+
         A  |  C
     F---|--|-E---+
         |  |  |  D
         +B-+  +--+

    ...the packet would go:

    6 steps down (including the first line at the top of the diagram).
    3 steps right.
    4 steps up.
    3 steps right.
    4 steps down.
    3 steps right.
    2 steps up.
    13 steps left (including the F it stops on).

    This would result in a total of 38 steps.

    How many steps does the packet need to go?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from vector import Vector


def solve(pipes):
    """Return the number of steps the packet takes, given the diagram.

    :pipes: ASCII representation of the network pipes
    :returns: number of steps

    >>> solve('''     |
    ...      |  +--+
    ...      A  |  C
    ...  F---|----E|--+
    ...      |  |  |  D
    ...      +B-+  +--+''')
    38
    """
    grid = {}

    for y, row in enumerate(pipes.split('\n')):
        for x, c in enumerate(row):
            if not c.isspace():
                grid[Vector(x, y)] = c

    pos = next(v for v, c in grid.items() if v.y == 0)
    direction = Vector(0, 1)
    steps = 0

    while True:
        if pos not in grid:
            # walked off the grid, we're done

            return steps

        if grid[pos].isalpha():
            pass
        elif grid[pos] == '+':
            # change direction
            left = pos + direction.left()
            right = pos + direction.right()

            if left in grid and not grid[left].isspace():
                direction = direction.left()
            elif right in grid and not grid[right].isspace():
                direction = direction.right()
            else:
                # couldn't go left or right
                assert False
        else:
            assert not grid[pos].isspace()
        pos = pos + direction
        steps += 1


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
