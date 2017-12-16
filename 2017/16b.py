#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    16b.py
    ~~~~~~
    Advent of Code 2017 - Day 16: Permuatation Promenade
    Part Two

    Now that you're starting to get a feel for the dance moves, you turn your
    attention to the dance as a whole.

    Keeping the positions they ended up in from their previous dance, the
    programs perform it again and again: including the first dance, a total of
    one billion (1000000000) times.

    In the example above, their second dance would begin with the order baedc,
    and use the same dance moves:

     - s1, a spin of size 1: cbaed.
     - x3/4, swapping the last two programs: cbade.
     - pe/b, swapping programs e and b: ceadb.

    In what order are the programs standing after their billion dances?

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
    """Return program order after doing all the moves, one billion times.

    :moves: dance moves, separated by commas
    :nr: number of programs
    :returns: program order

    >>> solve('s1,x3/4,pe/b', nr=5)
    'abcde'
    """

    pgms = list(string.ascii_lowercase[:nr])
    cycle = None
    stop = 1e9

    for dance in range(1000000000):
        if cycle and dance % cycle == stop:
            # we can stop early if we've detected a cycle and our
            # dance round is relative to the end dance round

            return ''.join(pgms)

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

        if not cycle and ''.join(pgms) == string.ascii_lowercase[:nr]:
            # detected a cycle, calculate when we can stop early
            cycle = dance + 1
            stop = 1e9 % cycle

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
