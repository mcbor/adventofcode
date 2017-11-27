#!/usr/bin/env python3
# Advent of Code 2016 - Day 7, Part One

import sys
import re
from itertools import islice

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result
        
def has_abba(string):
    for s in window(string, 4):
        if s[:2] == s[:1:-1] and s[0] != s[1]:
            return True
    return False


def main(argv):
    if len(argv) < 2:
        print("Usage: day07-pt1.py puzzle.txt")
        return 1
    valid = 0
    with open(argv[1]) as f:
        for line in f:
            nets = re.split('[\[\]]', line.strip())
            if any(has_abba(s) for s in nets[::2]) \
                and not any(has_abba(h) for h in nets[1::2]):
                valid += 1
    print(valid)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
