#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    01b.py
    ~~~~~~
    Advent of Code 2017 - Day 1: Inverse Captcha
    Part Two

    Now, instead of considering the next digit, it wants you to consider
    the digit halfway around the circular list. That is, if your list
    contains 10 items, only include a digit in your sum if the digit 10/2
    = 5 steps forward matches it. Fortunately, your list has an even
    number of elements.

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(captcha):
    """Solve captcha.

    :input: captcha string
    :return: sum of all paired digits that match 
    
    >>> solve('1212')
    6
    >>> solve('1221')
    0
    >>> solve('123425')
    4
    >>> solve('123123')
    12
    >>> solve('12131415')
    4
    """
    captcha = list(map(int, captcha))
    return sum(x for n, x in enumerate(captcha) if x == captcha[(n+len(captcha)//2) % len(captcha)])


def main(argv):
    if len(argv) < 2:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    else:
        f = open(sys.argv[1], 'r')

    for input in f:
        print(solve(input.strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
