#!/usr/bin/env python3
# Advent of Code 2016 - Day 1, Part Two
# Using turtle graphics to find the location of Easter Bunny HQ.
# It's slow, but draws pretty maps.

import sys
import turtle

def distance():
    return round(abs(turtle.xcor() + abs(turtle.ycor())))


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
        
    with open(argv[1]) as f:
        visited = set()
        
        # init turtle to face north
        turtle.speed('fastest')
        turtle.home()
        turtle.setheading(90)
        visited.add(turtle.position())
        
        for line in f:
            if line[0] == '#':
                # skip comments
                continue
            steps = line.split()
            for step in map(str.strip, line.split(',')):
                direction = step[0]
                moves = int(step[1:])
                if direction == 'R':
                    turtle.right(90)
                elif direction == 'L':
                    turtle.left(90)
                else:
                    print("don't know about", direction)
                    return 1
                for _ in range(moves):
                    turtle.forward(1)
                    if turtle.position() in visited:
                        print("Visited {} twice, we're there! Distance: {}".format(turtle.position(), distance()))
                        input("Press any key to exit...")
                        return 0
                    else:
                        visited.add(turtle.position())
                
                print(step + ": " + str(turtle.position()))
        print("Stopped at {}, Distance: {}".format(str(turtle.position()), distance()))
        input("Press any key to exit...")
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))