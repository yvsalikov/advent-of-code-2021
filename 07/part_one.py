# Advent of Code 2021
# https://adventofcode.com/2021
# Day 7: The Treachery of Whales

from functools import reduce

with open("input.txt") as file:
    crabs = [int(crab_pos) for crab_pos in file.readline().rstrip().split(",")]

# Find median
crabs.sort()
median = abs(crabs[len(crabs) // 2])
fuel = reduce(lambda acc, pos: acc + abs(median - pos), crabs, 0)
print(f"It will take {fuel} fuel to arrange crabs to position {median}")
