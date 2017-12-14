#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    14a.py
    ~~~~~~
    Advent of Code 2017 - Day 14: Disk Defragmentation
    Part One

    Suddenly, a scheduled job activates the system's disk defragmenter. Were
    the situation different, you might sit and watch it for a while, but today,
    you just don't have that kind of time. It's soaking up valuable system
    resources that are needed elsewhere, and so the only option is to help it
    finish its task as soon as possible.

    The disk in question consists of a 128x128 grid; each square of the grid is
    either free or used. On this disk, the state of the grid is tracked by the
    bits in a sequence of knot hashes.

    A total of 128 knot hashes are calculated, each corresponding to a single
    row in the grid; each hash contains 128 bits which correspond to individual
    grid squares. Each bit of a hash indicates whether that square is free (0)
    or used (1).

    The hash inputs are a key string (your puzzle input), a dash, and a number
    from 0 to 127 corresponding to the row. For example, if your key string
    were flqrgnkx, then the first row would be given by the bits of the knot
    hash of flqrgnkx-0, the second row from the bits of the knot hash of
    flqrgnkx-1, and so on until the last row, flqrgnkx-127.

    The output of a knot hash is traditionally represented by 32 hexadecimal
    digits; each of these digits correspond to 4 bits, for a total of
    4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its
    equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001,
    e becomes 1110, f becomes 1111, and so on; a hash that begins with
    a0c2017... in hexadecimal would begin with
    10100000110000100000000101110000... in binary.

    Continuing this process, the first 8 rows and columns for key flqrgnkx
    appear as follows, using # to denote used squares, and . to denote free
    ones:

    # .#.#..-->
    .#.#.#.#
    ....#.#.
    #.#.##.#
    .##.#...
    ##..#..#
    .#...#..
    # .#.##.-->
    |      |
    V      V

    In this example, 8108 squares are used across the entire 128x128 grid.

    Given your actual key string, how many squares are used?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from operator import xor
from itertools import zip_longest
from functools import reduce

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

    >>> knothash('')
    'a2582a3a0e66e6e86e3812dcb672a272'
    >>> knothash('AoC 2017')
    '33efeb34ea91902bb2f59c9920caa6cd'
    >>> knothash('1,2,3')
    '3efbe78a8d82f29979031a4aa0b16a9d'
    >>> knothash('1,2,4')
    '63960835bcdc130f0b66d7ff4f6a5a8e'
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
    dense_hash = []

    for block in blocks:
        dense_hash.append(reduce(xor, block))

    return ''.join(f"{x:02x}" for x in dense_hash)


def solve(key):
    """Return number of squares used.

    :key: initial key string
    :returns: number of squares used

    >>> solve('flqrgnkx')
    8108
    """
    grid = [knothash(f"{key}-{row}") for row in range(128)]

    return sum(f"{int(r, 16):128b}".count('1') for r in grid)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
