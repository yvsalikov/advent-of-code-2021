# Advent of Code 2021
# https://adventofcode.com/2021
# Day 17: Trick Shot

import re
from math import sqrt, floor, ceil
from collections import namedtuple

Limits = namedtuple("Limits", "minimum maximum")

def steps_to_stop_in(target: Limits) -> Limits:
    # Find first term of arithmetic sequence that sums to target and stops.
    # Sum of _coordinates_ v0 + (v0 - 1) + (v0 - 2) + ... + 1 should be in target range. Find v0.
    # This sum is v0*(v0 + 1) / 2 (sum of first v0 integers).
    minimum = ceil((sqrt(8*abs(target.minimum) - 3) - 1)/2)
    maximum = floor((sqrt(8*abs(target.maximum) - 3) - 1)/2)
    return Limits(min(minimum, maximum), max(minimum, maximum))
    
def step(x0, y0, vx0, vy0):
    x = x0 + vx0
    y = y0 + vy0
    vx = vx0 - 1 if vx0 != 0 else 0
    vy = vy0 - 1
    return (x, y, vx, vy)
    
def brute_count_hits(x_target: Limits, y_target: Limits) -> int:
    # Brute force
    vx_max = x_target.maximum
    x_steps = steps_to_stop_in(x_target)
    vx_min = x_steps.minimum
    # Suppose y_target values is always negative
    vy_min = y_target.minimum
    vy_max = -y_target.minimum # fire up with the same velocity
    
    hits = 0
    for vx0 in range(vx_min, vx_max + 1):
        for vy0 in range(vy_min, vy_max + 1):
            vy = vy0
            vx = vx0
            x = y = 0
            while True:
                x, y, vx, vy = step(x, y, vx, vy)
                if x > x_target.maximum or y < y_target.minimum:
                    break
                if (x_target.minimum <= x <= x_target.maximum and 
                    y_target.minimum <= y <= y_target.maximum):
                    hits += 1
                    break
    return hits


with open("input.txt") as file:
    m = re.match("target area: x=(-*\d+)..(-*\d+), y=(-*\d+)..(-*\d+)", file.readline())
x_target = Limits(int(m.group(1)), int(m.group(2)))
y_target = Limits(int(m.group(3)), int(m.group(4)))

print(brute_count_hits(x_target, y_target))

