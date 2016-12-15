#!/usr/bin/env python3
# Advent of Code 2016 - Day 15, Part One

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
            discs += [(positions, init)]
    t = 1
    while True:
        d = [(init+index+t) % positions for index, (positions, init) in enumerate(discs)]
        if not any(d):
            break
        t += 1
    print(t-1)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
