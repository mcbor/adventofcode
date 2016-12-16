#!/usr/bin/env python3
# Advent of Code 2016 - Day 15

import sys


def gen_dragon(a):
    invert = str.maketrans('01', '10')
    while True:
        b = a[::-1]
        b = b.translate(invert)
        result = a + '0' + b
        yield result
        a = result


def checksum(dragon):
    chk = [a == b and '1' or '0' for a, b in zip(dragon[::2], dragon[1::2])]
    while len(chk) % 2 == 0:
        chk = [a == b and '1' or '0' for a, b in zip(chk[::2], chk[1::2])]
    return chk


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1

    with open(argv[1]) as f:
        for line in f:
            seed, length = line.strip().split()
            length = int(length)
            dragon = seed
            gdragon = gen_dragon(seed)
            while len(dragon) < length:
                dragon = next(gdragon)
            print("".join(checksum(dragon[:length])))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
