#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    23a.py
    ~~~~~~
    Advent of Code 2017 - Day 23: Coprocessor Conflagration
    Part One

    You decide to head directly to the CPU and fix the printer from there. As
    you get close, you find an experimental coprocessor doing so much work that
    the local programs are afraid it will halt and catch fire. This would cause
    serious issues for the rest of the computer, so you head in and see what
    you can do.

    The code it's running seems to be a variant of the kind you saw recently on
    that tablet. The general functionality seems very similar, but some of the
    instructions are different:

     - set X Y sets register X to the value of Y.
     - sub X Y decreases register X by the value of Y.
     - mul X Y sets register X to the result of multiplying the value contained
       in register X by the value of Y.
     - jnz X Y jumps with an offset of the value of Y, but only if the value of
       X is not zero. (An offset of 2 skips the next instruction, an offset of
       -1 jumps to the previous instruction, and so on.)

    Only the instructions listed above are used. The eight registers here,
    named a through h, all start at 0.

    The coprocessor is currently set to some kind of debug mode, which allows

    for testing, but prevents it from doing any meaningful work.

    If you run the program (your puzzle input), how many times is the mul
    instruction invoked?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from collections import defaultdict

regs = defaultdict(int)


def load(n):
    if n.isalpha():
        return regs[n]

    return int(n)


def solve(instructions):
    """Return number mul instructions executed.

    :instructions: list of instructions, separated by newlines
    :returns: number mul instructions executed

    >>> solve('''set a 1
    ... add a 2
    ... mul a a
    ... mod a 5
    ... mul a 3
    ... set a 0
    ... mul a 3
    ... jgz a -1
    ... set a 1
    ... jgz a -2''')
    3
    """

    instructions = [tuple(line.split()) for line in instructions.split('\n')]

    pc = 0
    n = len(instructions)
    multiplications = 0

    while 0 <= pc < n:
        opcode, *args = instructions[pc]

        if opcode == 'set':
            regs[args[0]] = load(args[1])
        elif opcode == 'sub':
            regs[args[0]] -= load(args[1])
        elif opcode == 'mul':
            multiplications += 1
            regs[args[0]] *= load(args[1])
        elif opcode == 'jnz':
            if load(args[0]) != 0:
                pc += load(args[1])

                continue
        pc += 1

    return multiplications


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
