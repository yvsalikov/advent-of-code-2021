# Advent of Code 2021
# https://adventofcode.com/2021
# Day 14: Extended Polymerization

from collections import defaultdict

class Polymerization:
    rules_cache = {}
    def __init__(self, filename) -> None:
        with open(filename) as file:
            self.template = file.readline().rstrip()
            file.readline()
            for line in file:
                key, inside_char = line.rstrip().split(" -> ")
                self.rules_cache[key] = key[:1] + inside_char + key[-1:]
    
    def polymerise_once(self, poly: str) -> str:
        if poly in self.rules_cache:
            # print("\tfrom cache")
            poly = self.rules_cache[poly]
            # print(f"\t-> {poly}")
            return poly
        else:
            mid = len(poly) // 2
            left_poly = self.polymerise_once(poly[:mid + 1])
            right_poly = self.polymerise_once(poly[mid:])
            next_poly = left_poly[:-1] + right_poly
            # print(f"\tcacheing {poly} -> {next_poly}")
            self.rules_cache[poly] = next_poly
            poly = next_poly
            
        return poly
        
        
    def polymerise(self, steps: int) -> str:
        poly = self.template
        for step in range(steps):
            # print(f"{pol} -> ", end="")
            poly = self.polymerise_once(poly)
            # print(pol)
        return poly


if __name__ == '__main__':
    
    poly = Polymerization("input.txt")
    polymer_10 = poly.polymerise(40)
    counter = defaultdict(int)
    for c in polymer_10:
        counter[c] += 1
    
    sorted_keys = sorted(counter.items(), key=lambda n: n[1])
    print(sorted_keys[-1][1] - sorted_keys[0][1])
    
    
