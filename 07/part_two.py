# Advent of Code 2021
# https://adventofcode.com/2021
# Day 7: The Treachery of Whales

from functools import reduce
from statistics import mean
from math import floor

with open("input.txt") as file:
    crabs = [int(crab_pos) for crab_pos in file.readline().rstrip().split(",")]

# Find average value
avrg = floor(mean(crabs)) # Why floor() and not round()?
# print(avrg)
# 1. Find distanses to mean value.
# 2. Find fuel needed (sum of arithmetic progression).
# 3. Sum all values.
# Chaining maps and reduce for fun. :)
fuel = reduce(lambda a, p: a + p, map(lambda n: n*(n+1)//2, map(lambda x: abs(avrg - x), crabs)), 0)
print(f"It will take {fuel} fuel to arrange crabs to position {avrg}")
