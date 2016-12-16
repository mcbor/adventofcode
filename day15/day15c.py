#!/usr/bin/env python3
# Advent of Code 2016 - Day 15, variant C

import sys
import re

def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    discs = []
    with open(argv[1]) as f:
        for line in f:
            disc, positions, t0, init = map(int, re.findall(r'(\d+)', line))
            discs += [(positions, init + disc)]
    t = delta = 1
    for positions, init in discs:
        while (init + t) % positions != 0:
            t += delta
        delta *= positions
    print(t)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
