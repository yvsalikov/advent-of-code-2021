# Advent of Code 2020
# https://adventofcode.com/2020
# Day 7: Handy Haversacks

import re

bags = {}
with open("input-test.txt") as file:
    for line in file:
        bag_rules = [m.group(1) for m in re.finditer("(\w+ \w+) bags*", line.strip())]
        print(bag_rules)
        # bag = bag_rules[0]
        # for innerbag in bag_rules[1:]:
            # # https://stackoverflow.com/questions/42424611/creating-a-dictionary-of-sets/42424819
            # try:
                # bags[bag_rules[0]].add(innerbag)
            # except KeyError:
                # bags[bag_rules[0]] = {innerbag}

# print(bags)
# print()
# outbags = set()
# count_outside_bags(bags, "shiny gold", outbags)
# print(len(outbags) - 1)
