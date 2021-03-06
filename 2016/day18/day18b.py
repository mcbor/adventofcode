#!/usr/bin/env python3
# Advent of Code 2016 - Day 18

import sys
from operator import or_
from functools import reduce

def main(argv):
    if len(argv) < 3:
        print("Usage: {} puzzle.txt rows".format(argv[0]))
        return 1
    nrows = int(argv[2])
    with open(argv[1]) as f:
        for line in f:
            seed = line.strip()
            length = len(seed)
            mask = 2**length - 1
            row = reduce(or_, ((c == '^') << (length - i - 1) for i, c in enumerate(seed)))
            safe_tiles = bin(row ^ mask).count('1')
            for _ in range(nrows - 1):
                row = (row << 1 ^ row >> 1) & mask
                safe_tiles += bin(row ^ mask).count('1')
            print(safe_tiles)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))