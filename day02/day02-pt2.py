#!/usr/bin/env python3
# Advent of Code 2016 - Day 2, Part Two

import sys
from turtle import Vec2D

keypad = [[None, None,  '1', None, None],
          [None,  '2',  '3',  '4', None],
          [ '5',  '6',  '7',  '8',  '9'],
          [None,  'A',  'B',  'C', None],
          [None, None,  'D', None, None]]

moves = { 'U' : Vec2D(-1,  0),
          'D' : Vec2D(+1,  0),
          'L' : Vec2D( 0, -1),
          'R' : Vec2D( 0, +1)
        }
        
def in_bounds(v):
    return all(0 <= d <= 4 for d in v) and vec2digit(v) is not None

def vec2digit(v):
    return keypad[v[0]][v[1]]

def main(argv):
    if len(sys.argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return(1)
    position = Vec2D(2, 0)
    with open(argv[1]) as f:
        for line in f:
            for move in line.strip():
                new_position = position + moves[move]
                if in_bounds(new_position):
                    position = new_position
            print(str(vec2digit(position)), end='')
    print()
    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))