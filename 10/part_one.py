# Advent of Code 2021
# https://adventofcode.com/2021
# Day 10: Syntax Scoring

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
opentags = ['(', '[', '{', '<']
closetags = {')': '(', ']': '[', '}': '{', '>': '<'}
count = {')': 0, ']': 0, '}': 0, '>': 0}

with open("input.txt") as file:
    for line in file:
        stack = []
        for tag in line.rstrip():
            # Is the first tag always open?
            if tag in opentags:
                stack.append(tag)
            else:
                if stack.pop() != closetags[tag]:
                    count[tag] += 1
                    break

score = 0
for t in [')', ']', '}', '>']:
    score += count[t]*points[t]
print(score)

