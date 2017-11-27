#!/usr/bin/env python3
# Advent of Code 2016 - Day 9, Part One

import sys

def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    with open(argv[1]) as f:
        for line in f:
            output = []
            line = line.strip()
            while True:
                head, sep, tail = line.partition('(')
                output.append(head)
                if sep:
                    head, sep, tail = tail.partition(')') 
                    count, repetitions = map(int, head.split('x'))
                    output.append(tail[:count] * repetitions)
                    line = tail[count:]
                else:
                    # we're done
                    break
            print(len("".join(output)))

        
if __name__ == '__main__':
    sys.exit(main(sys.argv))