#!/usr/bin/env python3
# Advent of Code 2016 - Day 5, Part Two

import sys
import itertools
from hashlib import md5

def gen_password(door_id):
    index = 0
    while True:
        string = door_id + str(index)
        digest = md5(string.encode('utf-8')).hexdigest()
        pos = int(digest[5], 16)
        if digest.startswith('00000') and pos < 8:
            yield pos, digest[6]
        index += 1
    
def main(argv):
    if len(argv) < 2:
        print("Usage: day05-pt2.py door_id")
        return 1
    door_id = argv[1]
    password = ['_']*8
    for pos, char in gen_password(door_id):
        if password[pos] is '_':
            password[pos] = char
            print("".join(password))
            if '_' not in password:
                return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))
        