#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    11a.py
    ~~~~~~
    Advent of Code 2017 - Day 11: Hex Ed
    Part One

    Crossing the bridge, you've barely reached the other side of the stream
    when a program comes up to you, clearly in distress. "It's my child
    process," she says, "he's gotten lost in an infinite grid!"

    Fortunately for her, you have plenty of experience with infinite grids.

    Unfortunately for you, it's a hex grid.

    The hexagons ("hexes") in this grid are aligned such that adjacent hexes
    can be found to the north, northeast, southeast, south, southwest, and
    northwest:

      \ n  /
    nw +--+ ne
      /    \
    -+      +-
      \    /
    sw +--+ se
      / s  \

    You have the path the child process took. Starting where he started, you
    need to determine the fewest number of steps required to reach him.
    (A "step" means to move from the hex you are in to any adjacent hex.)

    For example:

     - ne,ne,ne is 3 steps away.
     - ne,ne,sw,sw is 0 steps away (back where you started).
     - ne,ne,s,s is 2 steps away (se,se).
     - se,sw,se,sw,sw is 3 steps away (s,s,sw).

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
import operator
from functools import reduce


class Hex(object):
    """Point on a hexagonal grid."""

    def __init__(self, q, r, s=None):
        """Construct new point on hex grid, either using cube (x,y,z) or axial
        coordinates (q,r).

        :q: x-axis
        :r: y-axis
        :s: z-axis, derived from q and r if not specified

        """

        if s is None:
            s = -q - r
        assert(q + r + s == 0)

        self.q = q
        self.r = r
        self.s = s

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r, self.s + other.s)

    @property
    def length(self):
        return int((abs(self.q) + abs(self.r) + abs(self.s)) / 2)


directions = {
    'n': Hex(0, -1),
    'ne': Hex(1, -1),
    'se': Hex(1, 0),
    's': Hex(0, 1),
    'sw': Hex(-1, 1),
    'nw': Hex(-1, 0)}


def solve(steps):
    """Return distance from the origin after following the path given in steps.

    :steps: string of steps the child process took, separated by commas.
    :return: distance from the origin.

    >>> solve('ne,ne,ne')
    3
    >>> solve('ne,ne,sw,sw')
    0
    >>> solve('ne,ne,s,s')
    2
    >>> solve('se,sw,se,sw,sw')
    3
    """
    steps = [directions[s] for s in steps.split(',')]
    child = reduce(operator.add, steps)

    return child.length


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
