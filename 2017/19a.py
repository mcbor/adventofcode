#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    19a.py
    ~~~~~~
    Advent of Code 2017 - Day 19: A Series of Tubes
    Part One

    Somehow, a network packet got lost and ended up here. It's trying to follow
    a routing diagram (your puzzle input), but it's confused about where to go.

    Its starting point is just off the top of the diagram. Lines (drawn with |,
    -, and +) show the path it needs to take, starting by going down onto the
    only line connected to the top of the diagram. It needs to follow this path
    until it reaches the end (located somewhere within the diagram) and stop
    there.

    Sometimes, the lines cross over each other; in these cases, it needs to

    continue going the same direction, and only turn left or right when there's
    no other option. In addition, someone has left letters on the line; these
    also don't change its direction, but it can use them to keep track of where
    it's been. For example:

         |
         |  +--+
         A  |  C
     F---|----E|--+
         |  |  |  D
         +B-+  +--+

    Given this diagram, the packet needs to take the following path:

    Starting at the only line touching the top of the diagram, it must go down,
    pass through A, and continue onward to the first +. Travel right, up, and
    right, passing through B in the process. Continue down (collecting C),
    right, and up (collecting D). Finally, go all the way left through E and
    stopping at F. Following the path to the end, the letters it sees on its
    path are ABCDEF.

    The little packet looks up at you, hoping you can help it find the way.
    What letters will it see (in the order it would see them) if it follows the
    path? (The routing diagram is very wide; make sure you view it without line
    wrapping.)

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""
import sys
from vector import Vector


def solve(pipes):
    """Return the path of the packet, given the diagram.

    :pipes: ASCII representation of the network pipes
    :returns: path of the packet

    >>> solve('''     |
    ...      |  +--+
    ...      A  |  C
    ...  F---|----E|--+
    ...      |  |  |  D
    ...      +B-+  +--+''')
    'ABCDEF'
    """
    grid = {}

    for y, row in enumerate(pipes.split('\n')):
        for x, c in enumerate(row):
            if not c.isspace():
                grid[Vector(x, y)] = c

    pos = next(v for v, c in grid.items() if v.y == 0)
    direction = Vector(0, 1)
    path = []

    while True:
        if pos not in grid:
            # walked off the grid, we're done

            return ''.join(path)

        if grid[pos].isalpha():
            path.append(grid[pos])
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


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
