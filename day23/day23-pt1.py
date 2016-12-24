#!/usr/bin/env python3
# Advent of Code 2016 - Day 23, Part One

import sys

reg = { 'pc': 0,
        'a':  7,
        'b':  0,
        'c':  0,
        'd':  0}
program = []


def cpy(x, y):
    try:
        a = int(x)
    except ValueError:
        a = reg[x]
    reg[y] = a
    reg['pc'] += 1


def inc(x):
    reg[x] += 1
    reg['pc'] += 1


def dec(x):
    reg[x] -= 1
    reg['pc'] += 1


def jnz(x, y):
    try:
        t = int(x)
    except ValueError:
        t = reg[x]
        
    try:
        offset = int(y)
    except ValueError:
        offset = reg[y]

    if t != 0:
        reg['pc'] += offset
    else:
        reg['pc'] += 1
        
def tgl(x):
    offset = x.isdigit() and int(x) or reg[x]
    index = reg['pc'] + offset
    if index >= 0 and index < len(program):
        instr = program[index][0]
        if instr is cpy:
            program[index][0] = jnz
        elif instr is inc:
            program[index][0] = dec
        elif instr is dec:
            program[index][0] = inc
        elif instr is jnz:
            program[index][0] = cpy
        elif instr is tgl:
            program[index][0] = inc
    reg['pc'] += 1
        


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    with open(argv[1]) as f:
        for line in f:
            cmd, *args = line.strip().split()
            if cmd == 'cpy':
                program.append([cpy, (args[0], args[1])])
            elif cmd == 'inc':
                program.append([inc, (args[0])])
            elif cmd == 'dec':
                program.append([dec, (args[0])])
            elif cmd == 'jnz':
                program.append([jnz, (args[0], args[1])])
            elif cmd == 'tgl':
                program.append([tgl, (args[0])])
            else:
                sys.stderr.write('err?\n')
    while reg['pc'] < len(program):
        program[reg['pc']][0](*program[reg['pc']][1])
    print(reg)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
