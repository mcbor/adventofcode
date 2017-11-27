#!/usr/bin/env python3
# Advent of Code 2016 - Day 3, Part One

import sys

with open(sys.argv[1]) as f:
    possible = 0
    for line in f:
        segments = [int(n) for n in line.split()]
        if 2*max(segments) < sum(segments):
            possible += 1
    print("{} possible triangle{}".format(possible, possible > 1 and 's' or '' ))