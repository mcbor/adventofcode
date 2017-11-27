#!/usr/bin/env python3
# Advent of Code 2016 - Day 8, Part One and Two

import sys
from itertools import chain

COLS = 50
ROWS = 6


def rect(display, x, y):
    for r in range(y):
        for c in range(x):
            display[r][c] = '#'


def rotate_col(display, x, s):
    d = list(zip(*display))
    rotate_row(d, x, s)
    display[:] = list(map(list, zip(*d)))


def rotate_row(display, y, s):
    display[y] = display[y][-s:] + display[y][:-s]


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    display = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    with open(argv[1]) as f:
        for line in f:
            cmd, *args = line.strip().split()
            print(line.strip())
            if cmd == 'rect':
                x, y = map(int, args[0].split('x'))
                rect(display, x, y)
            elif cmd == 'rotate':
                d = int(args[1].split('=')[1])
                s = int(args[3])
                if args[0] == 'column':
                    rotate_col(display, d, s)
                elif args[0] == 'row':
                    rotate_row(display, d, s)
                else:
                    print('err?', cmd, args)
                    return 1
            else:
                print('err?', cmd, args)
                return 1
            for row in display:
                print("".join(row))
    print("".join(chain.from_iterable(display)).count('#'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
