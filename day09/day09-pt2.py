#!/usr/bin/env python3
# Advent of Code 2016 - Day 9, Part Two

import sys

def decompress(string):
    size = 0
    head, sep, tail = string.partition('(')
    size += len(head)
    if sep:
        head, sep, tail = tail.partition(')') 
        count, repetitions = map(int, head.split('x'))        
        size += repetitions * decompress(tail[:count]) + decompress(tail[count:])
    return size

def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    with open(argv[1]) as f:
        for line in f:
            print(decompress(line.strip()))
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))