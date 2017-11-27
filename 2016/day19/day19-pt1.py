#!/usr/bin/env python3
# Advent of Code 2016 - Day 19, Part One

import sys

def main(argv):
    if len(argv) < 2:
        elves = 3005290
    else:
        elves = int(argv[2])
    print(int(bin(elves)[3:] + '1', 2))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))