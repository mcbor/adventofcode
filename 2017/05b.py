#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    05b.py
    ~~~~~~
    Advent of Code 2017 - Day 4: A Maze of Twisty Trampolines, All Alike
    Part Two

    Now, the jumps are even stranger: after each jump, if the offset was three
    or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

    Using this rule with the above example, the process now takes 10 steps, and
    the offset values after finding the exit are left as 2 3 2 3 -1.

    How many steps does it now take to reach the exit?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(jumplist):
    """Calculate number of steps needed to exit the maze

    :jumplist: list of jump instructions
    :return: number of steps to jump out of the list

    >>> solve([0, 3, 0, 1, -3])
    10
    """
    pc = 0
    steps = 0

    while 0 <= pc < len(jumplist):
        jump = jumplist[pc]
        jumplist[pc] += 1 if jump < 3 else -1
        pc += jump
        steps += 1

    return steps


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve([int(x) for x in f.read().strip().split('\n')]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
