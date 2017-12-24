#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    20b.py
    ~~~~~~
    Advent of Code 2017 - Day 20: Particle Swarm
    Part Two

    To simplify the problem further, the GPU would like to remove any particles
    that collide. Particles collide if their positions ever exactly match.
    Because particles are updated simultaneously, more than two particles can
    collide at the same time and place. Once particles collide, they are
    removed and cannot collide with anything else after that tick.

    For example:

    p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
    p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
    p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
    p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>

    p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>
    p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
    p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)
    p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>

    p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>
    p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
    p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)
    p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>

    ------destroyed by collision------
    ------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
    ------destroyed by collision------                      (3)
    p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>

    In this example, particles 0, 1, and 2 are simultaneously destroyed at the
    time and place marked X. On the next tick, particle 3 passes through
    unharmed.

    How many particles are left after all collisions are resolved?

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
    """Return number of particles after resolving all collisions.

    :system: particle initial system with position, velocity and acceleration
             vectors
    :returns: number of particles after resolving all collisions.

    >>> solve('''p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
    ... p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
    ... p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
    ... p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>''')
    1
    """
    particles = []

    for i, line in enumerate(system.strip().split('\n')):
        vectors = line.strip().split(', ')
        p, v, a = (Vector(*map(int, v[3:-1].split(','))) for v in vectors)
        particles.append(Particle(i, p, v, a))

    for tick in range(2000):
        for p in particles:
            p.update()
        seen = set()
        dupes = set()

        for p in particles:
            if p.p in seen:
                dupes.add(p.p)
            seen.add(p.p)
        particles = [p for p in particles if p.p not in dupes]

    return len(particles)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
    print(solve(f.read()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
