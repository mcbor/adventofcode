#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    03b.py
    ~~~~~~
    Advent of Code 2017 - Day 3: Spiral Memory
    Part Two

    As a stress test on the system, the programs here clear the grid and then
    store the value 1 in square 1. Then, in the same allocation order as shown
    above, they store the sum of the values in all adjacent squares, including
    diagonals.

    So, the first few squares' values are chosen as follows:

    - Square 1 starts with the value 1.
    - Square 2 has only one adjacent filled square (with value 1), so it also
      stores 1.
    - Square 3 has both of the above squares as neighbors and stores the sum of
      their values, 2.
    - Square 4 has all three of the aforementioned squares as neighbors and
     stores the sum of their values, 4.
    - Square 5 only has the first and fourth squares as neighbors, so it gets
      the value 5.

    Once a square is written, its value does not change. Therefore, the first
    few squares would receive the following values:

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...

    What is the first value written that is larger than your puzzle input?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from itertools import count, product
from math import ceil, sqrt


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


def fill():
    """Fill the spiral memory, yielding each new value.

    >>> f = fill()
    >>> next(f)
    1
    >>> next(f)
    1
    >>> next(f)
    2
    >>> [next(f) for _ in range(10)]
    [4, 5, 10, 11, 23, 25, 26, 54, 57, 59]
    >>> [next(f) for _ in range(10)]
    [122, 133, 142, 147, 304, 330, 351, 362, 747, 806]
    """
    memory = {(0, 0): 1}
    neighbors = list(product((-1, 0, 1), repeat=2))

    for n in count(1):
        x, y = spiral(n)
        coord = [(x + nb[0], y + nb[1]) for nb in neighbors]
        val = sum(map(lambda v: memory.get(v, 0), coord))
        memory[(x, y)] = val
        yield val


def solve(limit):
    """Calculate first value written larger than limit.

    :input: limit
    :return: first value written larger than limit

    >>> solve(1)
    2
    >>> solve(12)
    23
    >>> solve(23)
    25
    >>> solve(1024)
    1968
    """

    for n in fill():
        if n > limit:
            return n


def main(argv):
    if len(argv) == 2:
        print(solve(int(argv[1])))
    else:
        print("Usage: {} LIMIT".format(argv[0]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
