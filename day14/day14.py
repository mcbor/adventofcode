#!/usr/bin/env python3
# Advent of Code 2016 - Day 14, Part One
# salt: ngcjuoqr
# part one: 18626
# part two: 20092

import sys
from hashlib import md5
from itertools import islice, chain
from collections import defaultdict
from pprint import pprint

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


def gen_hash(salt, stretch=0):
    index = 0
    while True:
        string = salt + str(index)
        digest = md5(string.encode('utf-8')).hexdigest()
        for _ in range(stretch):
            digest = md5(digest.encode('utf-8')).hexdigest()
        yield index, digest
        index += 1


def char_in_row(hash, n):
    for w in window(hash, n):
        if all(w[0] == c for c in w):
            return w[0]
    return None


def main(argv):
    if len(argv) < 2:
        print("Usage: {} salt [stretch]".format(argv[0]))
        return 1
    salt = argv[1]
    if len(argv) > 2:
        stretch = int(argv[2])
    else:
        stretch = 0

    ghash = gen_hash(salt, stretch)
    candidates = defaultdict(list)
    valid = set()
    while True:
        index, digest = next(ghash)
        c3 = char_in_row(digest, 3)
        c5 = char_in_row(digest, 5)
        if c5 in candidates:
            valid |= set([(idx, hsh)
                          for idx, hsh in candidates[c5]
                          if (index - idx) > 0 and (index - idx) <= 1000])
        if c3 is not None:
            candidates[c3] += [(index, digest)]
            
        if len(valid) > 64:
            if sorted(valid)[63][0] + 1000 < index:
                break
    print(sorted(list(valid))[63][0])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
