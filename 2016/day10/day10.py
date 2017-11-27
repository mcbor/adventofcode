#!/usr/bin/env python3
# Advent of Code 2016 - Day 10, Part One & Two

import sys
import re
from collections import defaultdict

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret

class Output():
    def __init__(self, nr):
        self.nr = nr
        self.chip = None
        
    def give(self, chip):
        self.chip = chip

class Bot():    
    def __init__(self, nr):
        self.nr = nr
        self.low = None
        self.high = None
        self.chips = []
    
    def give(self, chip):
        self.chips.append(chip)
    
    def step(self):
        if len(self.chips) == 2:
            if 61 in self.chips and 17 in self.chips:
                print('bot {} compares 61 and 17'.format(self.nr))
            self.low.give(min(self.chips))
            self.high.give(max(self.chips))
            self.chips = []
        return len(self.chips) != 0
        

def main(argv):
    if len(argv) < 2:
        print("Usage: {} puzzle.txt".format(argv[0]))
        return 1
    bots = keydefaultdict(Bot)
    outputs = keydefaultdict(Output)
    with open(argv[1]) as f:
        for line in f:
            head, tail = line.split(maxsplit=1)
            if head == 'value':
                chip, bot = map(int, re.findall(r'(\d+)', tail))
                bots[bot].give(chip)
            elif head == 'bot':
                parts = tail.split()
                bot, low_id, high_id = map(int, re.findall(r'(\d+)', tail))
                low_type = parts[4]
                high_type = parts[9]
                if low_type == 'output':
                    bots[bot].low = outputs[low_id]
                else:
                    bots[bot].low = bots[low_id]
                if high_type == 'output':
                    bots[bot].high = outputs[high_id]
                else:
                    bots[bot].high = bots[high_id]
            else:
                print('err?', line)
        while True:
            result = [bot.step() for bot in bots.values()]
            if not any(result):
                break
        print(outputs[0].chip * outputs[1].chip * outputs[2].chip)
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))