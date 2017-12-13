#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    13a.py
    ~~~~~~
    Advent of Code 2017 - Day 13: Packet Scanners
    Part One

    You need to cross a vast firewall. The firewall consists of several layers,
    each with a security scanner that moves back and forth across the layer.
    To succeed, you must not be detected by a scanner.

    By studying the firewall briefly, you are able to record (in your puzzle
    input) the depth of each layer and the range of the scanning area for the
    scanner within it, written as depth: range. Each layer has a thickness of
    exactly 1. A layer at depth 0 begins immediately inside the firewall; a
    layer at depth 1 would start immediately after that.

    For example, suppose you've recorded the following:

    0: 3
    1: 2
    4: 4
    6: 4

    This means that there is a layer immediately inside the firewall (with
    range 3), a second layer immediately after that (with range 2), a third
    layer which begins at depth 4 (with range 4), and a fourth layer which
    begins at depth 6 (also with range 4).

    [...]

    Within each layer, a security scanner moves back and forth within its
    range. Each security scanner starts at the top and moves down until it
    reaches the bottom, then moves up until it reaches the top, and repeats. A
    security scanner takes one picosecond to move one step.

    [...]

    Your plan is to hitch a ride on a packet about to move through the
    firewall. The packet will travel along the top of each layer, and it moves
    at one layer per picosecond. Each picosecond, the packet moves one layer

    forward (its first move takes it into layer 0), and then the scanners move
    one step. If there is a scanner at the top of the layer as your packet
    enters it, you are caught. (If a scanner moves into the top of its layer

    while you are there, you are not caught: it doesn't have time to notice you
    before you leave.)

    [...]

    In this situation, you are caught in layers 0 and 6, because your packet
    entered the layer when its scanner was at the top when you entered it. You
    are not caught in layer 1, since the scanner moved into the top of the
    layer once you were already there.

    The severity of getting caught on a layer is equal to its depth multiplied
    by its range. (Ignore layers in which you do not get caught.) The severity
    of the whole trip is the sum of these values. In the example above, the
    trip severity is 0*3 + 6*4 = 24.

    Given the details of the firewall you've recorded, if you leave
    immediately, what is the severity of your whole trip?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def solve(firewall):
    """Return severity if the trip through the firewall.

    :firewall: list of depth and range of the scanner (separated by a colon)
               for each layer (separated by newline)
    :returns: severity of a trip

    >>> solve('''0: 3
    ... 1: 2
    ... 4: 4
    ... 6: 4''')
    24
    """

    scanners = {int(d) : int(r) for d, r in [line.split(': ') for line in firewall.split('\n')]}

    severity = 0

    for i in range(max(scanners) + 1):
        try:
            p = i % (2 * scanners[i] - 2)

            if p == 0:
                severity += i * scanners[i]
        except KeyError:
            continue

    return severity


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
