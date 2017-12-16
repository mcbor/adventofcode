#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    16a.py
    ~~~~~~
    Advent of Code 2017 - Day 16: Permuatation Promenade
    Part One

    You come upon a very unusual sight; a group of programs here appear to be
    dancing.

    There are sixteen programs in total, named a through p. They start by
    standing in a line: a stands in position 0, b stands in position 1, and so
    on until p, which stands in position 15.

    The programs' dance consists of a sequence of dance moves:

     - Spin, written sX, makes X programs move from the end to the front, but
       maintain their order otherwise. (For example, s3 on abcde produces
       cdeab).
     - Exchange, written xA/B, makes the programs at positions A and B swap
       places.
     - Partner, written pA/B, makes the programs named A and B swap places.

    For example, with only five programs standing in a line (abcde), they could
    do the following dance:

     - s1, a spin of size 1: eabcd.
     - x3/4, swapping the last two programs: eabdc.
     - pe/b, swapping programs e and b: baedc.

    After finishing their dance, the programs end up in order baedc.

    You watch the dance for a while and record their dance moves (your puzzle
    input). In what order are the programs standing after their dance?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""
import sys
import string


def spin(pgms, move):
    """Spin the last move program to the front.

    >>> spin(['a', 'b', 'c', 'd', 'e'], 1)
    ['e', 'a', 'b', 'c', 'd']
    >>> spin(['a', 'b', 'c', 'd', 'e'], 3)
    ['c', 'd', 'e', 'a', 'b']
    """

    return pgms[-move:] + pgms[:-move]


def exchange(pgms, a, b):
    """Swap the programs at position a and b.

    >>> exchange(['e', 'a', 'b', 'c', 'd'], 3, 4)
    ['e', 'a', 'b', 'd', 'c']
    """
    res = pgms[:]
    res[a], res[b] = res[b], res[a]

    return res


def partner(pgms, a, b):
    """Swap the programs a and b.

    >>> partner(['e', 'a', 'b', 'd', 'c'], 'e', 'b')
    ['b', 'a', 'e', 'd', 'c']
    """
    a = pgms.index(a)
    b = pgms.index(b)

    return exchange(pgms, a, b)


def solve(moves, nr=16):
    """Return program order after doing all the moves.

    :moves: dance moves, separated by commas
    :nr: number of programs
    :returns: program order

    >>> solve('s1,x3/4,pe/b', nr=5)
    'baedc'
    """

    pgms = list(string.ascii_lowercase[:nr])

    for move in moves.split(','):
        if move[0] == 's':
            i = int(move[1:])
            pgms = spin(pgms, i)
        elif move[0] == 'x':
            a, b = (int(p) for p in move[1:].split('/'))
            pgms = exchange(pgms, a, b)
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            pgms = partner(pgms, a, b)

    return ''.join(pgms)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
