#!/usr/bin/env python3
# Advent of Code 2016 - Day 22
# Solved part two by hand from the pretty printed grid.

import sys
import re
from itertools import permutations
from collections import namedtuple

NodeDF = namedtuple('NodeDF', 'size used avail use')

nrex = re.compile(r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)'
                  r'\s+(?P<size>\d+)T'
                  r'\s+(?P<used>\d+)T'
                  r'\s+(?P<avail>\d+)T'
                  r'\s+(?P<use>\d+)%')


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    nodes = {}
    with open(argv[1]) as f:
        for line in f:
            m = nrex.search(line)
            if m:
                x, y, size, used, avail, use = map(int, m.groups())
                nodes[(x, y)] = NodeDF(size, used, avail, use)

        for y in range(31):
            sys.stdout.write('{0:02d}: '.format(y))
            for x in range(31):
                node = nodes[(x, y)]
                if node.used == 0:
                    sys.stdout.write('_')
                elif node.used > 100:
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('.')
            sys.stdout.write('\n')
        sys.stdout.write('\n')

        viable = []
        for a, b in permutations(nodes.keys(), 2):
            if nodes[a].used != 0 and nodes[b].avail >= nodes[a].used:
                viable += [(a, b)]
        print(len(viable))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
