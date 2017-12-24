#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    21a.py
    ~~~~~~
    Advent of Code 2017 - Day 21: Fractal Art
    Part One

    You find a program trying to generate some art. It uses a strange process
    that involves repeatedly enhancing the detail of an image through a set of
    rules.

    The image consists of a two-dimensional square grid of pixels that are
    either on (#) or off (.). The program always begins with this pattern:

    .#.
    ..#
    ###

    Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to
    have a size of 3.

    Then, the program repeats the following process:

    If the size is evenly divisible by 2, break the pixels up into 2x2 squares,
    and convert each 2x2 square into a 3x3 square by following the
    corresponding enhancement rule. Otherwise, the size is evenly divisible by
    3; break the pixels up into 3x3 squares, and convert each 3x3 square into a
    4x4 square by following the corresponding enhancement rule. Because each
    square of pixels is replaced by a larger one, the image gains pixels and so
    its size increases.

    The artist's book of enhancement rules is nearby (your puzzle input);
    however, it seems to be missing rules. The artist explains that sometimes,
    one must rotate or flip the input pattern to find a match. (Never rotate or
    flip the output pattern, though.) Each pattern is written concisely: rows
    are listed as single units, ordered top-down, and separated by slashes. For
    example, the following rules correspond to the adjacent patterns:

    ../.#  =  ..
              .#

                    .#.
    .#./..#/###  =  ..#
                    ###

                            #..#
    #..#/..../#..#/.##.  =  ....
                            #..#
                            .##.

    When searching for a rule to use, rotate and flip the pattern as necessary.

    For example, all of the following patterns match the same rule:

    .#.   .#.   #..   ###
    ..#   #..   #.#   ..#
    ###   ###   ##.   .#.

    Suppose the book contained the following two rules:

    ../.# => ##./#../...
    .#./..#/### => #..#/..../..../#..#

    As before, the program begins with this pattern:

    .#.
    ..#
    ###

    The size of the grid (3) is not divisible by 2, but it is divisible by 3.
    It divides evenly into a single square; the square matches the second rule,
    which produces:

    #..#
    ....
    ....
    #..#

    The size of this enhanced grid (4) is evenly divisible by 2, so that rule
    is used. It divides evenly into four squares:

    #.|.#
    ..|..
    --+--
    ..|..
    #.|.#

    Each of these squares matches the same rule (../.# => ##./#../...), three
    of which require some flipping and rotation to line up with the rule. The
    output for the rule is the same in all four cases:

    ##.|##.
    #..|#..
    ...|...
    ---+---
    ##.|##.
    #..|#..
    ...|...

    Finally, the squares are joined into a new grid:

    ##.##.
    #..#..
    ......
    ##.##.
    #..#..
    ......

    Thus, after 2 iterations, the grid contains 12 pixels that are on.

    How many pixels stay on after 5 iterations?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
import math
from typing import Dict, List, Tuple, Iterator

Grid = Tuple[Tuple[str, ...], ...]


def transform(grid: Grid, rules: Dict[Grid, Grid]) -> Grid:
    """Transform a (2x2 or 3x3) grid given the ruleset.

    A grid matches if any of its rotations and mirrored rotations matches a
    rule.

    :grid: 2x2 or 3x3 grid to transform
    :rules: dict of transformation rules
    :returns: transformed grid

    >>> grid = (('#', '.'), ('#', '.'))
    >>> rules = {(('#', '.'), ('#', '.')):
    ... (('#', '#', '#'), ('.', '.', '.'), ('#', '.', '#'))}
    >>> transform(grid, rules)
    (('#', '#', '#'), ('.', '.', '.'), ('#', '.', '#'))
    """

    for _ in range(2):
        for _ in range(4):
            if grid in rules:
                return rules[grid]
            grid = rotate(grid)
        grid = transpose(grid)
    assert False


def to_pattern(grid: Grid) -> str:
    """Convert grid into pattern.

    :grid: grid to convert
    :returns: grid in pattern form

    >>> to_pattern((('#', '#', '#'), ('.', '.', '.'), ('#', '.', '#')))
    '###/.../#.#'
    """

    return '/'.join(''.join(row) for row in grid)


def rotate(grid: Grid) -> Grid:
    """Rotate grid clockwise

    :grid: grid to rotate clockwise
    :returns: rotated grid

    >>> rotate(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    ((7, 4, 1), (8, 5, 2), (9, 6, 3))
    """

    return tuple(zip(*grid[::-1]))


def transpose(grid: Grid) -> Grid:
    """Transpose (flip) grid along the diagonal

    :grid: grid to flip
    :returns: grid flipped along the diagonal

    >>> transpose(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    ((1, 4, 7), (2, 5, 8), (3, 6, 9))
    """

    return tuple(zip(*grid))


def to_grid(pattern: str) -> Grid:
    """Convert a pattern into a grid

    :pattern: pattern to convert
    :returns: grid

    >>> to_grid('..#/##./#.#')
    (('.', '.', '#'), ('#', '#', '.'), ('#', '.', '#'))
    """

    return tuple(tuple(row) for row in pattern.split('/'))


def divide(grid: Grid) -> Iterator[Grid]:
    """Divide grid into 2x2 or 3x3 tiles

    :grid: NxN grid
    :returns: generator that yields 2x2 or 3x3 tiles, depending on whether the
              grid is divisible by 2 or 3.

    >>> g = divide((
    ... ('#', '.', '.', '.'),
    ... ('.', '.', '.', '.'),
    ... ('#', '.', '#', '.'),
    ... ('#', '#', '#', '#')))
    >>> next(g)
    (('#', '.'), ('.', '.'))
    >>> next(g)
    (('.', '.'), ('.', '.'))
    >>> next(g)
    (('#', '.'), ('#', '#'))
    >>> next(g)
    (('#', '.'), ('#', '#'))
    """
    step = 2 if len(grid) % 2 == 0 else 3

    for y in range(0, len(grid), step):
        for x in range(0, len(grid), step):
            yield tuple(tuple(grid[r][x:x + step]) for r in range(y, y + step))


def merge(tgrid: List[Grid]) -> Grid:
    """Combine a tiled grid into a single grid

    >>> merge([
    ... (('#', '.'), ('.', '.')),
    ... (('.', '.'), ('.', '.')),
    ... (('#', '.'), ('#', '#')),
    ... (('#', '.'), ('#', '#'))])
    (('#', '.', '.', '.'), ('.', '.', '.', '.'), ('#', '.', '#', '.'), ('#', '#', '#', '#'))
    """
    tiles_per_row = int(math.sqrt(len(tgrid)))
    grid = ()

    for tile_offset in range(0, tiles_per_row):
        for row in range(0, len(tgrid[0])):
            r = ()

            for tile in range(0, tiles_per_row):
                r += tgrid[tile + tile_offset * tiles_per_row][row]
            grid += (r,)

    return grid


def show(grid: Grid):
    """Pretty print a grid"""
    print('\n'.join(''.join(row) for row in grid))


def parse(rulebook: str) -> Dict[Grid, Grid]:
    """Parse rulebook.

    :rulebook: list of transformations
    :returns: dict with grid to grid transforms

    >>> parse('''../.# => ##./#../...
    ... .#./..#/### => #..#/..../..../#..#''')
    {(('.', '.'), ('.', '#')): (('#', '#', '.'), ('#', '.', '.'), ('.', '.', '.')), (('.', '#', '.'), ('.', '.', '#'), ('#', '#', '#')): (('#', '.', '.', '#'), ('.', '.', '.', '.'), ('.', '.', '.', '.'), ('#', '.', '.', '#'))}
    """
    rules = {}

    for line in rulebook.strip().split('\n'):
        src, dst = map(to_grid, line.strip().split(' => '))
        rules[src] = dst

    return rules


def solve(rulebook):
    """Count numer of on pixels after 5 iterations.

    :rulebook: list of enhancement rules
    :returns: number of on pixels after 5 iterations
    """
    rules = parse(rulebook)

    # start pattern
    grid = to_grid('.#./..#/###')

    for i in range(5):
        tiles = []

        for tile in divide(grid):
            tiles.append(transform(tile, rules))
        grid = merge(tiles)

    return to_pattern(grid).count('#')


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
