#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    06b.py
    ~~~~~~
    Advent of Code 2017 - Day 6: Memory Reallocation
    Part Two

    Out of curiosity, the debugger would also like to know the size of the
    loop: starting from a state that has already been seen, how many block
    redistribution cycles must be performed before that same state is seen
    again?

    In the previous example, 2 4 1 2 is seen again after four cycles, and so
    the answer in that example would be 4.

    How many cycles are in the infinite loop that arises from the configuration
    in your puzzle input?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from itertools import count


def solve(banks):
    """Calculate number of steps needed to exit the maze

    :banks: list of blocks in each bank
    :return: number of redistribtion cycles to loop

    >>> solve([0, 2, 7, 0])
    4
    """

    seen = set()
    loops = 0
    mark = 0

    for cycle in count(1):
        # find value and the index of the bank with the largest block
        m = max(banks)
        i = banks.index(m)

        # reset the largest bank
        banks[i] = 0

        # redistribute its blocks
        q, r = divmod(m, len(banks))
        banks = [x + q for x in banks]

        for j in range(r):
            banks[(i + j + 1) % len(banks)] += 1

        # check if we've seen this configuration before
        b = tuple(banks)

        if b in seen:
            loops += 1

            if loops > 1:
                return cycle - mark
            else:
                seen = set()
                mark = cycle
        seen.add(b)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve([int(x) for x in f.read().strip().split()]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
