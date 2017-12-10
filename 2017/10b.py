#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    10b.py
    ~~~~~~
    Advent of Code 2017 - Day 10: Knoth Hash
    Part Two

    The logic you've constructed forms a single round of the Knot Hash
    algorithm; running the full thing requires many of these rounds. Some input
    and output processing is also required.

    First, from now on, your input should be taken not as a list of numbers,
    but as a string of bytes instead. Unless otherwise specified, convert
    characters to bytes using their ASCII codes. This will allow you to handle
    arbitrary ASCII strings, and it also ensures that your input lengths are
    never larger than 255. For example, if you are given 1,2,3, you should
    convert it to the ASCII codes for each character: 49,44,50,44,51.

    Once you have determined the sequence of lengths to use, add the following
    lengths to the end of the sequence: 17, 31, 73, 47, 23. For example, if you
    are given 1,2,3, your final sequence of lengths should be
    49,44,50,44,51,17,31,73,47,23 (the ASCII codes from the input string
    combined with the standard length suffix values).

    Second, instead of merely running one round like you did above, run a total
    of 64 rounds, using the same length sequence in each round. The current
    position and skip size should be preserved between rounds. For example, if
    the previous example was your first round, you would start your second
    round with the same length sequence (3, 4, 1, 5, 17, 31, 73, 47, 23, now
    assuming they came from ASCII codes and include the suffix), but start with
    the previous round's current position (4) and skip size (4).

    Once the rounds are complete, you will be left with the numbers from 0 to
    255 in some order, called the sparse hash. Your next task is to reduce
    these to a list of only 16 numbers called the dense hash. To do this, use
    numeric bitwise XOR to combine each consecutive block of 16 numbers in the
    sparse hash (there are 16 such blocks in a list of 256 numbers). So, the
    first element in the dense hash is the first sixteen elements of the sparse
    hash XOR'd together, the second element in the dense hash is the second
    sixteen elements of the sparse hash XOR'd together, etc.

    For example, if the first sixteen elements of your sparse hash are as shown
    below, and the XOR operator is ^, you would calculate the first output
    number like this:

    65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64

    Perform this operation on each of the sixteen blocks of sixteen numbers in
    your sparse hash to determine the sixteen numbers in your dense hash.

    Finally, the standard way to represent a Knot Hash is as a single
    hexadecimal string; the final output is the dense hash in hexadecimal
    notation. Because each number in your dense hash will be between 0 and 255
    (inclusive), always represent each number as two hexadecimal digits
    (including a leading zero as necessary). So, if your first three numbers
    are 64, 7, 255, they correspond to the hexadecimal numbers 40, 07, ff, and
    so the first six characters of the hash would be 4007ff. Because every
    Knot Hash is sixteen such numbers, the hexadecimal representation is always
    32 hexadecimal digits (0-f) long.

    Here are some example hashes:

     - The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
     - AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
     - 1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
     - 1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.

    Treating your puzzle input as a string of ASCII characters, what is the
    Knot Hash of your puzzle input? Ignore any leading or trailing whitespace
    you might encounter.

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from operator import xor
from itertools import cycle, islice, zip_longest
from functools import reduce

SUFFIX = [17, 31, 73, 47, 23]
MARKS = 256
ROUNDS = 64


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def circulair(lst, start, length):
    """Return a circulair (i.e. wrapping around) slice of lst of length
    'length', starting at 'start'.

    :lst: source list
    :start: start index of the slice
    :lenght: length of the slice
    :returns: circulair slice of lst
    """
    it = cycle(lst)
    next(islice(it, start, start), None)

    return list(islice(it, length))


def solve(string):
    """Calculate Knot Hash of the provided string.

    :string: input data string
    :returns: Knot Hash in dense hash form

    >>> solve('')
    'a2582a3a0e66e6e86e3812dcb672a272'
    >>> solve('AoC 2017')
    '33efeb34ea91902bb2f59c9920caa6cd'
    >>> solve('1,2,3')
    '3efbe78a8d82f29979031a4aa0b16a9d'
    >>> solve('1,2,4')
    '63960835bcdc130f0b66d7ff4f6a5a8e'
    """
    string = [ord(c) for c in string] + SUFFIX
    knots = list(range(MARKS))
    finger = skip = 0

    for _ in range(ROUNDS):
        lengths = string[:]

        for length in lengths:
            twist = circulair(knots, finger, length)[::-1]

            for i in range(length):
                knots[(finger + i) % MARKS] = twist[i]
            finger = (finger + length + skip) % MARKS
            skip += 1
    blocks = grouper(knots, 16)
    dense_hash = []
    for block in blocks:
        dense_hash.append(reduce(xor, block))
    return ''.join(f"{x:02x}" for x in dense_hash)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
