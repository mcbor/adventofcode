#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    04b.py
    ~~~~~~
    Advent of Code 2017 - Day 4: High-Entropy Passphrases
    Part Two

    For added security, yet another system policy has been put in place. Now, a
    valid passphrase must contain no two words that are anagrams of each
    other - that is, a passphrase is invalid if any word's letters can be
    rearranged to form any other word in the passphrase.

    For example:

    - 'abcde fghij' is a valid passphrase.
    - 'abcde xyz ecdab' is not valid - the letters from the third word can be
      rearranged to form the first word.
    - 'a ab abc abd abf abj' is a valid passphrase, because all letters need to
      be used when forming another word.
    - 'iiii oiii ooii oooi oooo' is valid.
    - 'oiii ioii iioi iiio' is not valid - any of these words can be rearranged
      to form any other word.

    Under this new system policy, how many passphrases are valid?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(passphrases):
    """Calculate number of valid passphrases.

    :passphrases: string of passphrases, separated by newlines
    :return: number of valid passphrases

    >>> solve('abcde fghij')
    1
    >>> solve('abcde xyz ecdab')
    0
    >>> solve('a ab abc abd abf abj')
    1
    >>> solve('iiii oiii ooii oooi oooo')
    1
    >>> solve('oiii ioii iioi iiio')
    0
    """
    valid = 0

    for passphrase in passphrases.split('\n'):
        words = passphrase.split()
        words = [''.join(word) for word in map(sorted, words)]

        if len(words) == len(set(words)):
            valid += 1

    return valid


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
