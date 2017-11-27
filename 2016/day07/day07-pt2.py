#!/usr/bin/env python3
# Advent of Code 2016 - Day 7, Part Two

import sys
import re
from itertools import islice, chain

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
        
def gen_aba(string):
    for s in window(string, 3):
        if s[0] != s[1] and s[0] == s[2]:
            yield s
            
def gen_bab(abas):
    for aba in abas:
        yield aba[1], aba[0], aba[1]

def main(argv):
    if len(argv) < 2:
        print("Usage: day07-pt2.py puzzle.txt")
        return 1
    valid = 0
    with open(argv[1]) as f:
        for line in f:
            nets = re.split('[\[\]]', line.strip())
            supernet_aba = (gen_aba(s) for s in nets[::2])
            hypernet_bab = (gen_bab(gen_aba(h)) for h in nets[1::2])
            aba_set = set(chain.from_iterable(supernet_aba))
            bab_set = set(chain.from_iterable(hypernet_bab))
            if not aba_set.isdisjoint(bab_set):
                valid += 1
    print(valid)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
