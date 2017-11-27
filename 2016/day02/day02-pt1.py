#!/usr/bin/env python3
# Advent of Code 2016 - Day 2, Part One

import sys
from turtle import Vec2D

moves = { 'U' : Vec2D( 0, -1),
          'D' : Vec2D( 0, +1),
          'L' : Vec2D(-1,  0),
          'R' : Vec2D(+1,  0)
        }
        
def in_bounds(v):
    return all(0 <= d <= 2 for d in v)

def vec2digit(v):
    return v[1] * 3 + v[0] + 1

def main(argv):
    if len(sys.argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return(1)
    position = Vec2D(1, 1)
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