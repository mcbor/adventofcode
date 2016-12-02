#!/usr/bin/env python3
# Advent of Code 2016 - Day 1
# Using turtle graphics to find the location of Easter Bunny HQ.
# It's slow, but draws pretty maps.

import sys
import turtle

if len(sys.argv) < 2:
    print("Usage: {} puzzle.txt".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1]) as f:
    # init turtle to face north
    turtle.speed('fastest')
    turtle.home()
    turtle.setheading(90)
        
    for line in f:
        if line[0] == '#':
            # skip comments
            continue
        steps = line.split()
        for step in map(str.strip, line.split(',')):
            if step[0] == 'R':
                turtle.right(90)
            elif step[0] == 'L':
                turtle.left(90)
            else:
                print("don't know about", step[0])
                sys.exit(1)
            turtle.forward(int(step[1:]))
            print(step + ": " + str(turtle.position()))
    print("Stopped at {}, Distance: {}".format(str(turtle.position()), round(abs(turtle.xcor()) + abs(turtle.ycor()))))
    input("Press any key to exit...")