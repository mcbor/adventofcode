#!/usr/bin/env python3
# Advent of Code 2016 - Day 20

import sys
from itertools import tee
from heapq import heappop, heappush
import re


def heapiterate(h):
    while len(h) > 0:
        yield heappop(h)


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    with open(argv[1]) as f:
        h = []
        allowed = 0
        # read and sort intervals
        for line in f:
            a, b = map(int, re.findall(r'(\d+)', line))
            heappush(h, [a,b])
        # merge intervals
        intervals = [heappop(h)]
        for next_range in heapiterate(h):
            if intervals[-1][1] + 1 < next_range[0]:
                allowed += next_range[0] - intervals[-1][1] - 1
                intervals.append(next_range)
            elif intervals[-1][1] < next_range[1]:
                intervals[-1][1] = next_range[1]
        print(intervals[0][1] + 1)
        print(allowed)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
