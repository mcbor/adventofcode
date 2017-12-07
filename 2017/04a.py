#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    04a.py
    ~~~~~~
    Advent of Code 2017 - Day 4: High-Entropy Passphrases
    Part One

    A new system policy has been put in place that requires all accounts to use
    a passphrase instead of simply a password. A passphrase consists of a
    series of words (lowercase letters) separated by spaces. To ensure
    security, a valid passphrase must contain no duplicate words.

    For example:

    - aa bb cc dd ee is valid.
    - aa bb cc dd aa is not valid - the word aa appears more than once.
    - aa bb cc dd aaa is valid - aa and aaa count as different words.

    The system's full passphrase list is available as your puzzle input. How
    many passphrases are valid?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(passphrases):
    """Calculate number of valid passphrases.

    :passphrases: string of passphrases, separated by newlines
    :return: number of valid passphrases

    >>> solve('aa bb cc dd ee')
    1
    >>> solve('aa bb cc dd aa')
    0
    >>> solve('aa bb cc dd aaa')
    1
    """

    return sum(len(words) == len(set(words))
               for words in (passphrase.split()
                             for passphrase in passphrases.split('\n')))


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
