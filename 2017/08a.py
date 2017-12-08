#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    08a.py
    ~~~~~~
    Advent of Code 2017 - Day 8: I Heard You Like Registers
    Part One

    You receive a signal directly from the CPU. Because of your recent
    assistance with jump instructions, it would like you to compute the result
    of a series of unusual register instructions.

    Each instruction consists of several parts: the register to modify,
    whether to increase or decrease that register's value, the amount by which
    to increase or decrease it, and a condition. If the condition fails, skip
    the instruction without modifying the register. The registers all start
    at 0. The instructions look like this:

      b inc 5 if a > 1
      a inc 1 if b < 5
      c dec -10 if a >= 1
      c inc -20 if c == 10

    These instructions would be processed as follows:

     - Because a starts at 0, it is not greater than 1, and so b is not
       modified.
     - a is increased by 1 (to 1) because b is less than 5 (it is 0).
     - c is decreased by -10 (to 10) because a is now greater than or equal
       to 1 (it is 1).
     - c is increased by -20 (to -10) because c is equal to 10.

    After this process, the largest value in any register is 1.

    You might also encounter <= (less than or equal to) or != (not equal to).
    However, the CPU doesn't have the bandwidth to tell you what all the
    registers are named, and leaves that to you to determine.

    What is the largest value in any register after completing the instructions
    in your puzzle input?

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
    """Find the largest value in any register after completion.

    :program: list of instructions, separated by newlines
    :return: largest value in any register

    >>> solve('''b inc 5 if a > 1
    ... a inc 1 if b < 5
    ... c dec -10 if a >= 1
    ... c inc -20 if c == 10''')
    1
    """

    regs = defaultdict(int)

    for line in program.split('\n'):
        r, op, val, _, cmp_reg, cmp_op, cmp_val = line.split()

        if ops[cmp_op](regs[cmp_reg], int(cmp_val)):
            regs[r] = ops[op](regs[r], int(val))

    return max(regs.values())


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
