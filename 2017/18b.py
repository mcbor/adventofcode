#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    18b.py
    ~~~~~~
    Advent of Code 2017 - Day 18: Duet
    Part Two

    As you congratulate yourself for a job well done, you notice that the
    documentation has been on the back of the tablet this entire time. While
    you actually got most of the instructions correct, there are a few key
    differences. This assembly code isn't about sound at all - it's meant to be
    run twice at the same time.

    Each running copy of the program has its own set of registers and follows
    the code independently - in fact, the programs don't even necessarily run
    at the same speed. To coordinate, they use the send (snd) and receive (rcv)
    instructions:

    snd X sends the value of X to the other program. These values wait in a
          queue until that program is ready to receive them. Each program has
          its own message queue, so a program can never receive a message it
          sent.
    rcv X receives the next value and stores it in register X. If no values are
          in the queue, the program waits for a value to be sent to it.
          Programs do not continue to the next instruction until they have
          received a value. Values are received in the order they are sent.

    Each program also has its own program ID (one 0 and the other 1); the
    register p should begin with this value.

    For example:

    snd 1
    snd 2
    snd p
    rcv a
    rcv b
    rcv c
    rcv d

    Both programs begin by sending three values to the other. Program 0 sends
    1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value
    (both 1) and stores it in a, receives another value (both 2) and stores it
    in b, and then each receives the program ID of the other program
    (program 0 receives 1; program 1 receives 0) and stores it in c. Each
    program now sees a different value in its own copy of register c.

    Finally, both programs try to rcv a fourth time, but no data is waiting for
    either of them, and they reach a deadlock. When this happens, both programs
    terminate.

    It should be noted that it would be equally valid for the programs to run
    at different speeds; for example, program 0 might have sent all three
    values and then stopped at the first rcv before program 1 executed even its
    first instruction.

    Once both of your programs have terminated (regardless of what caused them
    to do so), how many times did program 1 send a value?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
import threading
import queue
from collections import defaultdict


class Worker(threading.Thread):
    def __init__(self, pid, instructions, inq, outq):
        super().__init__()
        self.pid = pid
        self.instructions = instructions
        self.inq = inq
        self.outq = outq

        self.regs = defaultdict(int)
        self.regs['p'] = pid
        self.tx = 0
        self.pc = 0

    def load(self, n):
        if n.isalpha():
            return self.regs[n]

        return int(n)

    def run(self):
        while True:
            opcode, *args = self.instructions[self.pc]

            if opcode == 'snd':
                self.outq.put(self.load(args[0]))
                self.tx += 1
            elif opcode == 'set':
                self.regs[args[0]] = self.load(args[1])
            elif opcode == 'add':
                self.regs[args[0]] += self.load(args[1])
            elif opcode == 'mul':
                self.regs[args[0]] *= self.load(args[1])
            elif opcode == 'mod':
                self.regs[args[0]] %= self.load(args[1])
            elif opcode == 'rcv':
                try:
                    self.regs[args[0]] = self.inq.get(timeout=1)
                except queue.Empty:
                    # get timed out, so the other thread was probably
                    # also waiting. Return our tx
                    self.inq.put(self.tx)

                    return
            elif opcode == 'jgz':
                if self.load(args[0]) > 0:
                    self.pc += self.load(args[1])

                    continue
            else:
                assert False
            self.pc += 1


def solve(instructions):
    """Return how many times program 1 send a value when terminated.

    :instructions: list of instructions, separated by newlines
    :returns: number of transmissions for 1

    >>> solve('''snd 1
    ... snd 2
    ... snd p
    ... rcv a
    ... rcv b
    ... rcv c
    ... rcv d''')
    3
    """
    instructions = [tuple(line.split()) for line in instructions.split('\n')]
    q0, q1 = queue.Queue(), queue.Queue()
    w0 = Worker(0, instructions, q0, q1)
    w1 = Worker(1, instructions, q1, q0)
    w0.start()
    w1.start()
    w0.join()
    w1.join()

    return q1.get()


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
