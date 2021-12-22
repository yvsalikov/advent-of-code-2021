# Advent of Code 2021
# https://adventofcode.com/2021
# Day 17: Trick Shot

import re
from math import sqrt

with open("input_test.txt") as file:
    m = re.match("target area: x=(-*\d+)..(-*\d+), y=(-*\d+)..(-*\d+)", file.readline())
tx_min, tx_max, ty_min, ty_max = map(int, m.group(1, 2, 3, 4))

# The probe reaches the highest y position on trajectories for whitch x = const on falling slope.
# Therefore vx0 + (vx0 - 1) + (vx0 - 2) + ... 1 = 1 + 2 + 3 + ... + vx0 = vx0*(vx0 + 1)/2
# should be in range tx_min, tx_max
vx_min = int((sqrt(8*tx_min - 3) - 1)/2)
vx_max = int((sqrt(8*tx_max - 3) - 1)/2)

# If we fire out the probe with vertical velocity vy0 it reaches "ground" after 2*vy0 steps.
# Its vertical velocity will be -(vy0 + 1). Trajectories with higher y position have higher "ground" velocities.
# The highest y position is reached if the probe hits the target arrea on next step.
vy_min = min(-ty_min - 1, -ty_max - 1)
vy_max = max(-ty_min - 1, -ty_max - 1)

print(vx_min, vx_max)
print(vy_min, vy_max)

# The max y position is vy0 + (vy0 - 1) + (vy0 - 2) + ... 1 = 1 + 2 + 3 + ... + vy0 = vy0*(vy0 + 1)/2
highest_y_pos = vy_max * (vy_max + 1) // 2
print(highest_y_pos)

