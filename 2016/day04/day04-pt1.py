#!/usr/bin/env python3
# Advent of Code 2016 - Day 4, Part One

import sys
from operator import itemgetter

def valid(name, checksum):
    # count the letters, filtering out dashes
    letters = dict((c, name.count(c)) for c in set(name) if c != '-')
    # first sort by secondary key (letter)
    s = sorted(letters.items(), key=itemgetter(0))
    # then sort by primary key (occurrence) in reverse
    t = sorted(s, key=itemgetter(1), reverse=True)
    # 'calculate' the checksum
    c = "".join(q[0] for q in t)[:5]
    return c == checksum
    
def parse(line):
    line = line.strip()
    name, tail = line.rsplit('-', 1)
    sector = tail[0:tail.index('[')]
    checksum = tail[tail.index('['):].strip('[]')
    return name, int(sector), checksum

with open(sys.argv[1]) as f:
    sector_sum = 0
    for line in f:
        name, sector, checksum = parse(line)
        if valid(name, checksum):
            sector_sum += int(sector)    
    print(sector_sum)
        