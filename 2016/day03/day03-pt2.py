#!/usr/bin/env python3
# Advent of Code 2016 - Day 3, Part Two

import sys

with open(sys.argv[1]) as f:
    possible = 0
    triangles = [map(int, line.split()) for line in f]
    for i in range(0, len(triangles), 3):
        triangles[i:i+3] = zip(*triangles[i:i+3])
    possible = sum(2*max(triangle) < sum(triangle) for triangle in triangles)
    print("{} possible triangle{}".format(possible, possible > 1 and 's' or '' ))