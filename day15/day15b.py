#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Advent of Code 2016 - Day 15, variant B

import sys
import re
from functools import reduce

def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    conditions = []
    with open(argv[1]) as f:
        for line in f:
            disc, positions, _, init = map(int, re.findall(r'(\d+)', line))
            conditions += [((-init - disc) % positions, positions)]
    product = reduce(lambda x, y: x * y, (t[1] for t in conditions))
    sequences = [set(range(a, product, n)) for a, n in conditions]
    result = list(reduce(lambda x, y: x & y, sequences))
    print(result[0])
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))