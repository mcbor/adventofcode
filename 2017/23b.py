#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    23b.py
    ~~~~~~
    Advent of Code 2017 - Day 23: Coprocessor Conflagration
    Part Two

    Now, it's time to fix the problem.

    The debug mode switch is wired directly to register a. You flip the switch,
    which makes register a now start at 1 when the program is executed.

    Immediately, the coprocessor begins to overheat. Whoever wrote this program
    obviously didn't choose a very efficient implementation. You'll need to
    optimize the program if it has any hope of completing before Santa needs
    that printer working.

    The coprocessor's ultimate goal is to determine the final value left in
    register h once the program completes. Technically, if it had that... it
    wouldn't even need to run the program.

    After setting register a to 1, if the program were to run to completion,
    what value would be left in register h?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
import math


def is_prime(n):
    if n < 2:
        return False

    if n < 4:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def solve(instructions):
    """Return value of h.

    Hand optimized.
    """
    instr, reg, val = instructions.split('\n')[0].split()
    assert instr == 'set'
    assert reg == 'b'

    b = int(val) * 100 + 100000
    start = b - 17000
    end = b + 1

    return sum(not is_prime(x) for x in range(start, end, 17))


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
