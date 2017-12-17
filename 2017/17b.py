#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    17b.py
    ~~~~~~
    Advent of Code 2017 - Day 17: Spinlock
    Part Two

    The spinlock does not short-circuit. Instead, it gets more angry. At least, you assume that's what happened; it's spinning significantly faster than it was a moment ago.

    You have good news and bad news.

    The good news is that you have improved calculations for how to stop the spinlock. They indicate that you actually need to identify the value after 0 in the current state of the circular buffer.

    The bad news is that while you were determining this, the spinlock has just finished inserting its fifty millionth value (50000000).

    What is the value after 0 the moment 50000000 is inserted?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""
import sys


def solve(steps):
    """Return value next to 0 after 50 million insertions.

    :steps: number of steps before every insertion
    :returns: value next to 0

    >>> solve(3)
    1222153
    >>> solve(301)
    33601318
    """
    buffer = [0]
    c = 0
    res = 0
    for i in range(1, 50000000):
        c = (c + steps) % i + 1
        if c == 1:
            res = i
    return res

def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(int(f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
