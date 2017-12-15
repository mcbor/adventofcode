#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    15b.py
    ~~~~~~
    Advent of Code 2017 - Day 15: Dueling Generators
    Part Two

    In the interest of trying to align a little better, the generators get more
    picky about the numbers they actually give to the judge.

    They still generate values in the same way, but now they only hand a value
    to the judge when it meets their criteria:

    Generator A looks for values that are multiples of 4.
    Generator B looks for values that are multiples of 8.

    Each generator functions completely independently: they both go through
    values entirely on their own, only occasionally handing an acceptable value
    to the judge, and otherwise working through the same sequence of values as
    before until they find one.

    The judge still waits for each generator to provide it with a value before
    comparing them (using the same comparison method as before). It keeps track
    of the order it receives values; the first values from each generator are
    compared, then the second values from each generator, then the third
    values, and so on.

    Using the example starting values given above, the generators now produce
    the following first five values each:

    --Gen. A--  --Gen. B--
    1352636452  1233683848
    1992081072   862516352
     530830436  1159784568
    1980017072  1616057672
     740335192   412269392

    These values have the following corresponding binary values:

    01010000100111111001100000100100
    01001001100010001000010110001000

    01110110101111001011111010110000
    00110011011010001111010010000000

    00011111101000111101010001100100
    01000101001000001110100001111000

    01110110000001001010100110110000
    01100000010100110001010101001000

    00101100001000001001111001011000
    00011000100100101011101101010000

    Unfortunately, even though this change makes more bits similar on average,
    none of these values' lowest 16 bits match. Now, it's not until the 1056th
    pair that the judge finds the first match:

    --Gen. A--  --Gen. B--
    1023762912   896885216

    00111101000001010110000111100000
    00110101011101010110000111100000
    This change makes the generators much slower, and the judge is getting
    impatient; it is now only willing to consider 5 million pairs. (Using the
    values from the example above, after five million pairs, the judge would
    eventually find a total of 309 pairs that match in their lowest 16 bits.)

    After 5 million pairs, but using this new generator logic, what is the
    judge's final count?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""
import sys


FACTOR_A = 16807
FACTOR_B = 48271

CRITERIA_A = 4
CRITERIA_B = 8


def generator(init, factor, criteria):
    """Create a new generator, starting at init, multiplying each result with
    factor modules 2147483647.
    >>> a = generator(65, 16807, 4)
    >>> next(a)
    1352636452
    >>> next(a)
    1992081072
    >>> next(a)
    530830436
    >>> next(a)
    1980017072
    """
    n = init

    while True:
        n = (n * factor) % 2147483647

        if n % criteria == 0:
            yield n


def solve(init_a, init_b):
    """Return number of matching pairs.

    :init_a: initial value for Generator A
    :init_b: initial value for Generator B
    :returns: number of matchin pairs used

    >>> solve(65, 8921)
    309
    """

    gen_a = generator(init_a, FACTOR_A, CRITERIA_A)
    gen_b = generator(init_b, FACTOR_B, CRITERIA_B)
    match = 0

    for _ in range(5000000):
        if next(gen_a) & 0xffff == next(gen_b) & 0xffff:
            match += 1

    return match


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    init_a = int(f.readline().strip().split()[-1])
    init_b = int(f.readline().strip().split()[-1])
    print(solve(init_a, init_b))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
