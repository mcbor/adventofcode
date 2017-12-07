#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    02a.py
    ~~~~~~
    Advent of Code 2017 - Day 2: Corruption Checksum
    Part One

    The spreadsheet consists of rows of apparently-random numbers. To make sure
    the recovery process is on the right track, they need you to calculate the
    spreadsheet's checksum. For each row, determine the difference between the
    largest value and the smallest value; the checksum is the sum of all of
    these differences.

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(spreadsheet):
    """Calculate checksum.

    :input: spreadsheet
    :return: checksum

    >>> solve('5\\t1\\t9\\t5\\n7\\t5\\t3\\n2\\t4\\t6\\t8')
    18
    """
    chksum = 0

    for row in spreadsheet.split('\n'):
        numbers = [int(x) for x in row.split('\t')]
        chksum += max(numbers) - min(numbers)

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
