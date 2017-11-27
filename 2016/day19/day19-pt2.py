#!/usr/bin/env python3
# Advent of Code 2016 - Day 19, Part One

import sys
from math import log

def main(argv):
    if len(argv) < 2:
        elves = 3005290
    else:
        elves = int(argv[2])
    t = 3**int(log(elves, 3))
    if elves == t:
        n = elves
    else:
        n = max(elves - t, 2*elves - 3*t)
    print(n)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))