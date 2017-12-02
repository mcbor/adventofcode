#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    02b.py
    ~~~~~~
    Advent of Code 2017 - Day 2: Corruption Checksum
    Part Two

    It sounds like the goal is to find the only two numbers in each row where
    one evenly divides the other - that is, where the result of the division
    operation is a whole number. They would like you to find those numbers on
    each line, divide them, and add up each line's result.

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from itertools import permutations


def solve(spreadsheet):
    """Calculate checksum.

    :input: spreadsheet
    :return: checksum

    >>> solve('5\\t9\\t2\\t8\\n9\\t4\\t7\\t3\\n3\\t8\\t6\\t5')
    9
    """
    chksum = 0
    for row in spreadsheet.split('\n'):
        numbers = [int(x) for x in row.split('\t')]
        for x, y in permutations(numbers, 2):
            quotient, remainder = divmod(x, y)
            if remainder == 0:
                chksum += quotient
    return chksum


def main(argv):
    if len(argv) < 2:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    else:
        f = open(sys.argv[1], 'r')
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
