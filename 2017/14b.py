#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    14b.py
    ~~~~~~
    Advent of Code 2017 - Day 14: Disk Defragmentation
    Part Two

    Now, all the defragmenter needs to know is the number of regions. A region
    is a group of used squares that are all adjacent, not including diagonals.
    Every used square is in exactly one region: lone used squares form their
    own isolated regions, while several adjacent squares all count as a single
    region.

    In the example above, the following nine regions are visible, each marked
    with a distinct digit:

    11.2.3..-->
    .1.2.3.4
    ....5.6.
    7.8.55.9
    .88.5...
    88..5..8
    .8...8..
    88.8.88.-->
    |      |
    V      V

    Of particular interest is the region marked 8; while it does not appear
    contiguous in this small view, all of the squares marked 8 are connected
    when considering the whole 128x128 grid. In total, in this example, 1242
    regions are present.

    How many regions are present given your key string?
    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from operator import xor
from itertools import zip_longest
from functools import reduce
from collections import deque

NEIGHBOURS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
SUFFIX = [17, 31, 73, 47, 23]
MARKS = 256
ROUNDS = 64


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n

    return zip_longest(*args, fillvalue=fillvalue)


def reverse(src, start, length):
    """Reverse a sublist, wrapping around.

    :src: source list
    :start: start of the sublist
    :length: length of the sublist
    :returns: new list with the elements from start till
              (start+length) % len(src) reversed

    >>> x = [1, 2, 3, 4, 5]
    >>> reverse(x, 2, 4)
    [3, 2, 1, 5, 4]
    >>> reverse(x, 0, 2)
    [2, 1, 3, 4, 5]
    >>> reverse(x, 4, 2)
    [5, 2, 3, 4, 1]
    """
    size = len(src)
    dst = src[:]

    for i in range(length // 2):
        a = (i + start) % size
        b = ((start + length) - i - 1) % size
        dst[a], dst[b] = src[b], src[a]

    return dst


def knothash(key):
    """Calculate Knot Hash of the provided key.

    :key: input data string
    :returns: Knot Hash in dense hash form

    >>> hex(knothash(''))
    '0xa2582a3a0e66e6e86e3812dcb672a272'
    >>> hex(knothash('AoC 2017'))
    '0x33efeb34ea91902bb2f59c9920caa6cd'
    >>> hex(knothash('1,2,3'))
    '0x3efbe78a8d82f29979031a4aa0b16a9d'
    >>> hex(knothash('1,2,4'))
    '0x63960835bcdc130f0b66d7ff4f6a5a8e'
    """
    string = [ord(c) for c in key] + SUFFIX
    knots = list(range(MARKS))
    finger = skip = 0

    for _ in range(ROUNDS):
        lengths = string[:]

        for length in lengths:
            knots = reverse(knots, finger, length)
            finger = (finger + length + skip) % MARKS
            skip += 1
    blocks = grouper(knots, 16)
    dense_hash = 0

    for block in blocks:
        dense_hash = (dense_hash << 8) | reduce(xor, block)

    return dense_hash


def solve(key):
    """Return number of regions in the grid.

    :key: initial key string
    :returns: number of regions

    >>> solve('flqrgnkx')
    1242
    """
    hashes = (knothash(f"{key}-{row}") for row in range(128))
    grid = (f"{h:0128b}" for h in hashes)
    squares = set()

    for y, row in enumerate(grid):
        for x, bit in enumerate(row):
            if bit == '1':
                squares.add((x, y))
    groups = []

    while squares:
        visited = set()
        queue = deque([squares.pop()])

        while queue:
            v = queue.popleft()
            visited.add(v)
            adjacent = set((v[0]+dx, v[1]+dy) for dx, dy in NEIGHBOURS)
            to_visit = (adjacent & squares) - visited
            queue.extend(to_visit)
        groups.append(visited)
        squares -= visited

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
