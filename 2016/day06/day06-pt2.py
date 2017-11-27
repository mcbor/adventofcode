#!/usr/bin/env python3
# Advent of Code 2016 - Day 6, Part Two

import sys
from collections import defaultdict
from operator import itemgetter


def main(argv):
    if len(argv) < 2:
        print("Usage: day06-pt1.py puzzle.txt")
        return 1
    columns = defaultdict(lambda: defaultdict(int))
    with open(argv[1]) as f:
        for line in f:
            for i, c in enumerate(line.strip()):
                columns[i][c] += 1
    for i in sorted(columns.keys()):
        sys.stdout.write(sorted(columns[i].items(), key=itemgetter(1))[0][0])
    print()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
