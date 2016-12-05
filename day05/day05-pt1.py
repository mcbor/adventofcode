#!/usr/bin/env python3
# Advent of Code 2016 - Day 5, Part One

import sys
import itertools
from hashlib import md5

def gen_password(door_id):
    index = 0
    while True:
        string = door_id + str(index)
        digest = md5(string.encode('utf-8')).hexdigest()
        if digest.startswith('00000'):
            yield digest[5]
        index += 1
    
def main(argv):
    if len(argv) < 2:
        print("Usage: day05-pt1.py door_id")
        return 1
    door_id = argv[1]
    password = itertools.islice(gen_password(door_id), 8)
    print("".join(password))
    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))
        