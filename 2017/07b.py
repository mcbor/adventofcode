#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    07b.py
    ~~~~~~
    Advent of Code 2017 - Day 7: Recursive Circus
    Part Two

    The programs explain the situation: they can't get down. Rather, they could
    get down, if they weren't expending all of their energy trying to keep the
    tower balanced. Apparently, one program has the wrong weight, and until it's
    fixed, they're stuck here.

    For any program holding a disc, each program standing on that disc forms a
    sub-tower. Each of those sub-towers are supposed to be the same weight, or
    the disc itself isn't balanced. The weight of a tower is the sum of the
    weights of the programs in that tower.

    In the example before, this means that for ugml's disc to be balanced, gyxo,
    ebii, and jptl must all have the same weight, and they do: 61.

    However, for tknk to be balanced, each of the programs standing on its disc
    and all programs above it must each match. This means that the following
    sums must all be the same:

    ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
    padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
    fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

    As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
    other two. Even though the nodes above ugml are balanced, ugml itself is too
    heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep
    the towers balanced. If this change were made, its weight would be 60.

    Given that exactly one program is the wrong weight, what would its weight
    need to be to balance the entire tower?

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

    def balance(self):
        """Total weight of this subtree and its children"""

        return self.weight + sum(child.balance() for child in self.children)

    def is_balanced(self):
        """Return true if all children are balanced, false otherwise"""

        return len(set(child.balance() for child in self.children)) == 1

    def __repr__(self):
        return f"{self.name} ({self.weight})"


def solve(tower):
    """Figure out the correct weight.

    :tower: list of programs with their weight and balancing programs,
            if holding a disc
    :return: the correct weight

    >>> solve("pbga (66)\\nxhth (57)\\nebii (61)\\nhavc (66)\\nktlj (57)\\nfwft (72) -> ktlj, cntj, xhth\\nqoyq (66)\\npadx (45) -> pbga, havc, qoyq\\ntknk (41) -> ugml, padx, fwft\\njptl (61)\\nugml (68) -> gyxo, ebii, jptl\\ngyxo (61)\\ncntj (57)")
    60
    """

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

    # pick a node and follow its parent up until we got one without a parent
    root = nodes[list(nodes)[0]]

    while root.parent:
        root = root.parent

    # start at the root
    node = root

    while True:
        # find the unbalanced child and go from there
        for child in node.children:
            if not child.is_balanced():
                node = child
                break
        else:
            # we get here if all children's children of this node are balanced
            # so one of its children is the unbalanced one
            weights = [child.balance() for child in node.children]
            idx, = [i for i, w in enumerate(weights) if weights.count(w) == 1]
            offbalance = node.children[idx]
            diff = weights[idx] - weights[not idx]

            return offbalance.weight - diff


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
