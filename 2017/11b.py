#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    11b.py
    ~~~~~~
    Advent of Code 2017 - Day 11: Hex Ed
    Part Two

    How many steps away is the furthest he ever got from his starting position?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


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
    2
    >>> solve('ne,ne,s,s')
    2
    >>> solve('se,sw,se,sw,sw')
    3
    """
    steps = [directions[s] for s in steps.split(',')]
    furthest = 0
    child = Hex(0, 0)

    for step in steps:
        child += step
        furthest = max(furthest, child.length)

    return furthest


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
