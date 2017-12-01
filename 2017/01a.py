#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    01a.py
    ~~~~~~
    Advent of Code 2017 - Day 1: Inverse Captcha
    Part One

    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list. The
    list is circular, so the digit after the last digit is the first digit in
    the list.

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(captcha):
    """Solve captcha.

    :input: captcha string
    :return: sum of all paired digits that match 
    
    >>> solve('1122')
    3
    >>> solve('1111')
    4
    >>> solve('98769')
    9
    """
    captcha = list(map(int, captcha))
    return sum(x for n, x in enumerate(captcha) if x == captcha[(n+1) % len(captcha)])


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
