#!/usr/bin/env python3
# Advent of Code 2016 - Day 25

import sys
from itertools import count

reg = { 'pc':   0,
        'a':    0,
        'b':    0,
        'c':    0,
        'd':    0,
        'out': [0]}
program = []

def cpy(x, y):
    if x in reg:
        a = reg[x]
    else:
        a = int(x)
    reg[y] = a
    reg['pc'] += 1


def inc(x):
    reg[x] += 1
    reg['pc'] += 1


def dec(x):
    reg[x] -= 1
    reg['pc'] += 1


def jnz(x, y):
    if x in reg:
        t = reg[x]
    else:
        t = int(x)

    if y in reg:
        offset = reg[y]
    else:
        offset = int(y)

    if t != 0:
        reg['pc'] += offset
    else:
        reg['pc'] += 1
        
def tgl(x):
    if x in reg:
        offset = reg[x]
    else:
        offset = int(x)
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
        

def out(x):
    if x in reg:
        output = reg[x]
    else:
        output = int(x)
    if output not in (0,1) or output == reg['out'][-1]:
        raise Exception
    reg['out'] += [output]
    reg['pc'] += 1
    
def reset():
    reg['a'] = 0
    reg['b'] = 0
    reg['c'] = 0
    reg['d'] = 0
    reg['pc'] = 0
    reg['out'] = [1]
        

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
            elif cmd == 'out':
                program.append([out, (args[0])])
            else:
                sys.stderr.write('err?\n')
    for i in count(1):
        reset()
        reg['a'] = i
        iterations = 0
        try:
            while reg['pc'] < len(program) and len(reg['out']) < 10:
                program[reg['pc']][0](*program[reg['pc']][1])
                iterations += 1
            else:
                print(i)
                return 0
        except Exception:
            pass
       

if __name__ == '__main__':
    sys.exit(main(sys.argv))
