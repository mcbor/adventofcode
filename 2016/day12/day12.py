#!/usr/bin/env python3
# Advent of Code 2016 - Day 12, Part One & Two

import sys

register = {'a': 0,
            'b': 0,
            'c': 1,
            'd': 0}


def cpy(x, y):
    if x.isdigit():
        register[y] = int(x)
    else:
        register[y] = register[x]
    return 1


def inc(x):
    register[x] += 1
    return 1


def dec(x):
    register[x] -= 1
    return 1


def jnz(x, y):
    t = x.isdigit() and int(x) or register[x]
    if t != 0:
        return int(y)
    else:
        return 1


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    pc = 0
    program = []
    with open(argv[1]) as f:
        for line in f:
            cmd, *args = line.strip().split()
            if cmd == 'cpy':
                program.append((cpy, (args[0], args[1])))
            elif cmd == 'inc':
                program.append((inc, (args[0])))
            elif cmd == 'dec':
                program.append((dec, (args[0])))
            elif cmd == 'jnz':
                program.append((jnz, (args[0], args[1])))
    while pc < len(program):
        pc += program[pc][0](*program[pc][1])
    print(register)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
