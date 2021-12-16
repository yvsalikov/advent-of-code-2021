# Advent of Code 2021
# https://adventofcode.com/2021
# Day 14: Extended Polymerization

from collections import defaultdict

class Polymerization:
    def __init__(self, filename) -> None:
        self.rules = {}
        self.pairs_counter = {}
        with open(filename) as file:
            self.template = file.readline().rstrip()
            file.readline()
            for line in file:
                key, inside_char = line.rstrip().split(" -> ")
                self.rules[key] = [key[:1] + inside_char, inside_char + key[-1:]]
                self.pairs_counter[key] = 0
        for i in range(len(self.template) - 1):
            self.pairs_counter[self.template[i:i+2]] += 1
    
    def polymerise(self, steps: int) -> None:
        for i in range(steps):
            prev_pairs_counter = list(self.pairs_counter.items())
            for pair, count in prev_pairs_counter:
                if count > 0:
                    # parent pairs die
                    self.pairs_counter[pair] -= count
                    # two new pairs born
                    for new_pair in self.rules[pair]:
                        self.pairs_counter[new_pair] += count
    
    def most_minus_least_common_element(self) -> int:
        elements = defaultdict(int)
        # Pairs overlap, so count only the first element in a pair
        for pair, count in self.pairs_counter.items():
            elements[pair[0]] += count
        # Count last element of template
        elements[self.template[-1]] += 1
        sorted_elements = sorted(elements.items(), key=lambda count: count[1])
        return(sorted_elements[-1][1] - sorted_elements[0][1])
    
    
if __name__ == '__main__':
    polymer = Polymerization("input.txt")
    # polymer.polymerise(10)
    # print(polymer.most_minus_least_common_element())
    polymer.polymerise(40)
    print(polymer.most_minus_least_common_element())
    
