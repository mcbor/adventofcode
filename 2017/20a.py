#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    20a.py
    ~~~~~~
    Advent of Code 2017 - Day 20: Particle Swarm
    Part One

    Suddenly, the GPU contacts you, asking for help. Someone has asked it to
    simulate too many particles, and it won't be able to finish them all in
    time to render the next frame at this rate.

    It transmits to you a buffer (your puzzle input) listing each particle in
    order (starting with particle 0, then particle 1, particle 2, and so on).

    For each particle, it provides the X, Y, and Z coordinates for the
    particle's position (p), velocity (v), and acceleration (a), each in the

    format <X,Y,Z>.

    Each tick, all particles are updated simultaneously. A particle's
    properties are updated in the following order:

     - Increase the X velocity by the X acceleration.
     - Increase the Y velocity by the Y acceleration.
     - Increase the Z velocity by the Z acceleration.
     - Increase the X position by the X velocity.
     - Increase the Y position by the Y velocity.
     - Increase the Z position by the Z velocity.

    Because of seemingly tenuous rationale involving z-buffering, the GPU would
    like to know which particle will stay closest to position <0,0,0> in the
    long term. Measure this using the Manhattan distance, which in this
    situation is simply the sum of the absolute values of a particle's X, Y,
    and Z position.

    For example, suppose you are only given two particles, both of which stay
    entirely on the X-axis (for simplicity). Drawing the current states of
    particles 0 and 1 (in that order) with an adjacent a number line and
    diagram of current X positions (marked in parenthesis), the following would
    take place:

    p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

    p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

    p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

    p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)

    At this point, particle 1 will never be closer to <0,0,0> than particle 0,
    and so, in the long run, particle 0 will stay closest.

    Which particle will stay closest to position <0,0,0> in the long term?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from vector import Vector


class Particle(object):
    def __init__(self, i, p, v, a):
        self.i = i
        self.p = p
        self.v = v
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        self.update()

        return self

    def ff(self, t):
        """Fast forward the position by t ticks"""
        self.p = t**2 * self.a + t * self.v + self.p

    def update(self):
        """Update positon according to acceleration and velocity vectors"""
        self.v += self.a
        self.p += self.v

    def __abs__(self):
        """Return lenght of vector position"""
        return abs(self.p)

    def __repr__(self):
        return f"id={self.i}, p={self.p}, v={self.v}, a={self.a}"


def solve(system):
    """Return ID of particle who stays the closest to <0,0,0> in the long term.

    :system: particle initial system with position, velocity and acceleration
             vectors
    :returns: particle ID of the closest to <0,0,0> in the long term.

    >>> solve('''p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
    ... p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>''')
    0
    """
    particles = []

    for i, line in enumerate(system.strip().split('\n')):
        vectors = line.strip().split(', ')
        p, v, a = (Vector(*map(int, v[3:-1].split(','))) for v in vectors)
        particles.append(Particle(i, p, v, a))
    t = 10000

    for p in particles:
        p.ff(t)

    return sorted(particles, key=abs)[0].i


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
    print(solve(f.read()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
