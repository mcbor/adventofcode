#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    07a.py
    ~~~~~~
    Advent of Code 2017 - Day 7: Recursive Circus
    Part One

    Wandering further through the circuits of the computer, you come upon a
    tower of programs that have gotten themselves into a bit of trouble. A
    recursive algorithm has gotten out of hand, and now they're balanced
    precariously in a large tower.

    One program at the bottom supports the entire tower. It's holding a large
    disc, and on the disc are balanced several more sub-towers. At the bottom
    of these sub-towers, standing on the bottom disc, are other programs, each
    holding their own disc, and so on. At the very tops of these
    sub-sub-sub-...-towers, many programs stand simply keeping the disc below
    them balanced but with no disc of their own.

    You offer to help, but first you need to understand the structure of these
    towers. You ask each program to yell out their name, their weight, and
    (if they're holding a disc) the names of the programs immediately above
    them balancing on that disc. You write this information down (your puzzle
    input). Unfortunately, in their panic, they don't do this in an orderly
    fashion; by the time you're done, you're not sure which program gave which
    information.

    For example, if your list is the following:

    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)

    ...then you would be able to recreate the structure of the towers that
    looks like this:

                    gyxo
                  /
             ugml - ebii
           /      \
          |         jptl
          |
          |         pbga
         /        /
    tknk --- padx - havc
         \        \
          |         qoyq
          |
          |         ktlj
           \      /
             fwft - cntj
                  \
                    xhth

    In this example, tknk is at the bottom of the tower (the bottom program),
    and is holding up ugml, padx, and fwft. Those programs are, in turn,
    holding up other programs; in this example, none of those programs are
    holding up any other programs, and are all the tops of their own towers.
    (The actual tower balancing in front of you is much larger.)

    Before you're ready to help them, you need to make sure your information is
    correct. What is the name of the bottom program?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


class Node(object):
    def __init__(self, name, weight, parent=None, children=[]):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = children


def parse_input(tower):
    """Parse a tower input file into a dict of Node objects

    :tower: tower input file
    :returns: dict of Node objects with name as key"""
    nodes = {}

    # parse all input nodes

    for row in tower.split('\n'):
        name, weight, *tail = row.split()
        weight = int(weight[1:-1])
        children = [c.strip(', ') for c in tail[1:]] if tail else []
        nodes[name] = Node(name, weight, children=children)

    # correctly set all children and parent relations

    for name, node in nodes.items():
        node.children = [nodes[child] for child in node.children]

        for child in node.children:
            child.parent = node

    return nodes


def find_root(nodes):
    """Find the root of the tree

    :nodes: dict of Node objects
    :return: root Node"""

    # pick a node and follow its parent up until we got one without a parent
    root = next(iter(nodes.values()))

    while root.parent:
        root = root.parent

    return root


def solve(tower):
    """Find the bottom program (root) in the tower of programs

    :tower: list of programs with their weight and balancing programs,
            if holding a disc
    :return: bottom program

    >>> solve('''pbga (66)
    ... xhth (57)
    ... ebii (61)
    ... havc (66)
    ... ktlj (57)
    ... fwft (72) -> ktlj, cntj, xhth
    ... qoyq (66)
    ... padx (45) -> pbga, havc, qoyq
    ... tknk (41) -> ugml, padx, fwft
    ... jptl (61)
    ... ugml (68) -> gyxo, ebii, jptl
    ... gyxo (61)
    ... cntj (57)''')
    'tknk'
    """

    nodes = parse_input(tower)
    root = find_root(nodes)

    return root.name


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
