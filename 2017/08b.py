#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    08b.py
    ~~~~~~
    Advent of Code 2017 - Day 8: I Heard You Like Registers
    Part Two

    To be safe, the CPU also needs to know the highest value held in any
    register during this process so that it can decide how much memory to
    allocate to these operations. For example, in the previous instructions,
    the highest value ever held was 10 (in register c after the third
    instruction was evaluated).

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from collections import defaultdict
import operator

ops = {'<': operator.lt,
       '<=': operator.le,
       '==': operator.eq,
       '!=': operator.ne,
       '>=': operator.ge,
       '>': operator.gt,
       'inc': operator.add,
       'dec': operator.sub}


def solve(program):
    """Find the largest value ever held.

    :program: list of instructions, separated by newlines
    :return: largest value ever held

    >>> solve('''b inc 5 if a > 1
    ... a inc 1 if b < 5
    ... c dec -10 if a >= 1
    ... c inc -20 if c == 10''')
    10
    """

    regs = defaultdict(int)
    largest = 0

    for line in program.split('\n'):
        r, op, val, _, cmp_reg, cmp_op, cmp_val = line.split()

        if ops[cmp_op](regs[cmp_reg], int(cmp_val)):
            regs[r] = ops[op](regs[r], int(val))
            largest = max(largest, regs[r])

    return largest


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
