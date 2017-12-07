#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    03a.py
    ~~~~~~
    Advent of Code 2017 - Day 3: Spiral Memory
    Part One

    You come across an experimental new kind of memory stored on an infinite
    two-dimensional grid.

    Each square on the grid is allocated in a spiral pattern starting at a
    location marked 1 and then counting up while spiraling outward. For
    example, the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    While this is very space-efficient (no squares are skipped), requested data
    must be carried back to square 1 (the location of the only access port for
    this memory system) by programs that can only move up, down, left, or
    right. They always take the shortest path: the Manhattan Distance between
    the location of the data and square 1.

    For example:

    - Data from square 1 is carried 0 steps, since it's at the access port.
    - Data from square 12 is carried 3 steps, such as: down, left, left.
    - Data from square 23 is carried only 2 steps: up twice.
    - Data from square 1024 must be carried 31 steps.

    How many steps are required to carry the data from the square identified in
    your puzzle input all the way to the access port?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from math import ceil, sqrt


def manhattan(p, q):
    """Return Manhattan distance between two points

    :p: 2-tuple
    :q: 2-tuple
    :returns: Manhattan distance between p and q"""

    return int(abs(p[0] - q[0]) + abs(p[1] - q[1]))


def spiral(n):
    """Return Carthesian coordinates for point n on a spiral

    :n: spiral point
    :returns: Carthesian coordinate

    >>> spiral(1)
    (0, 0)
    >>> spiral(7)
    (-1, -1)
    >>> spiral(25)
    (2, -2)
    >>> spiral(-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 8, in spiral
    ValueError: math domain error
    """
    k = int(ceil((sqrt(n) - 1) / 2))
    t = 2 * k + 1
    m = t**2
    t = t - 1

    if n >= m - t:
        return k - (m - n), -k
    m = m - t

    if n >= m - t:
        return -k, -k + (m - n)
    m = m - t

    if n >= m - t:
        return -k + (m - n), k

    return k, k - (m - n - t)


def solve(n):
    """Calculate distance between square and the access port.

    :input: data square
    :return: distance to the access port

    >>> solve(1)
    0
    >>> solve(12)
    3
    >>> solve(23)
    2
    >>> solve(1024)
    31
    """

    return manhattan((0, 0), spiral(n))


def main(argv):
    if len(argv) == 2:
        print(solve(int(argv[1])))
    else:
        print("Usage: {} SQUARE".format(argv[0]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
