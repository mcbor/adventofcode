#!/usr/bin/env python3
# Advent of Code 2016 - Day 4, Part One

import sys
import string
from operator import itemgetter

def decode(ciphertext, shift):
    alphabet = string.ascii_lowercase
    shift = shift % len(alphabet)
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return ciphertext.translate(table)

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
    for line in f:
        name, sector, checksum = parse(line)
        if valid(name, checksum):
            print(decode(name, sector), sector)
