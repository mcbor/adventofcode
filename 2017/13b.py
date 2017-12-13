#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    13b.py
    ~~~~~~
    Advent of Code 2017 - Day 13: Packet Scanners
    Part Two

    Now, you need to pass through the firewall without being caught - easier
    said than done.

    You can't control the speed of the packet, but you can delay it any number
    of picoseconds. For each picosecond you delay the packet before beginning
    your trip, all security scanners move one step. You're not in the firewall
    during this time; you don't enter layer 0 until you stop delaying the
    packet.

    In the example above, if you delay 10 picoseconds (picoseconds 0 - 9),
    you won't get caught.

    [...]

    Because all smaller delays would get you caught, the fewest number of
    picoseconds you would need to delay to get through safely is 10.

    What is the fewest number of picoseconds that you need to delay the packet
    to pass through the firewall without being caught?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from itertools import count


def solve(firewall):
    """Return delay required to safely pass the firewall.

    :firewall: list of depth and range of the scanner (separated by a colon)
               for each layer (separated by newline)
    :returns: minium delay for a safe trip

    >>> solve('''0: 3
    ... 1: 2
    ... 4: 4
    ... 6: 4''')
    10
    """

    scanners = {int(d) : int(r) for d, r in [line.split(': ') for line in firewall.split('\n')]}

    layers = max(scanners) + 1

    for delay in count():
        for i in range(layers):
            try:
                p = (i+delay) % (2 * scanners[i] - 2)

                if p == 0:
                    break
            except KeyError:
                continue
        else:
            return delay


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
