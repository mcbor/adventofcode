#!/usr/bin/env python3
# Advent of Code 2016 - Day 21, Part Two

import sys
import re


def swap_position(string, x, y):
    string[x], string[y] = string[y], string[x]
    return string


def swap_letter(string, x, y):
    for i, c in enumerate(string):
        if c == x:
            string[i] = y
        elif c == y:
            string[i] = x
    return string


def rotate_right(string, n):
    n = n % len(string)
    return string[-n:] + string[:-n]
    

def rotate_left(string, n):
    return rotate_right(string, -n)


def rotate_position(string, x):
    i = string.index(x)
    n = i // 2 + (i % 2 == 1 or i == 0 and 1 or 5)
    return rotate_left(string, n)

def reverse(string, x, y):
    string[x:y+1] = string[x:y+1][::-1]
    return string


def move(string, x, y):
    c = string[x]
    del string[x]
    string.insert(y, c)
    return string


def getints(string):
    return map(int, re.findall(r'(\d+)', string))


def getchars(string):
    z = re.findall(r'(?:^|\s)([a-z])(?:\s|$)', string)
    return z


def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    with open(argv[1]) as f:
        string = list('fbgdceah')
        lines = reversed(f.readlines())
        for line in lines:
            head, tail = line.split(maxsplit=1)
            if head == 'swap':
                head, tail = tail.split(maxsplit=1)
                if head == 'position':
                    x, y = getints(tail)
                    string = swap_position(string, x, y)
                elif head == 'letter':
                    x, y = getchars(tail)
                    string = swap_letter(string, x, y)
            elif head == 'rotate':
                head, tail = tail.split(maxsplit=1)
                if head == 'left':
                    n = list(getints(tail))[0]
                    string = rotate_right(string, n)
                elif head == 'right':
                    n = list(getints(tail))[0]
                    string = rotate_left(string, n)
                else:
                    x = getchars(tail)[0]
                    string = rotate_position(string, x)
            elif head == 'reverse':
                x, y = getints(tail)
                string = reverse(string, x, y)
            elif head == 'move':
                x, y = getints(tail)
                string = move(string, y, x)
        print(''.join(string))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
