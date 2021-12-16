# Advent of Code 2021
# https://adventofcode.com/2021
# Day 10: Syntax Scoring

points = {')': 1, ']': 2, '}': 3, '>': 4}
opentags = {'(': ')', '[': ']', '{':'}', '<':'>'}
closetags = {')': '(', ']': '[', '}': '{', '>': '<'}
scores = []

with open("input.txt") as file:
    for line in file:
        stack = []
        iscorrupted = False
        for tag in line.rstrip():
            if tag in opentags:
                stack.append(tag)
            else:
                if stack.pop() != closetags[tag]:
                    iscorrupted = True
                    break
        
        if not iscorrupted:
            score = 0
            while stack:
                tag = stack.pop()
                score *= 5
                score += points[opentags[tag]]
            scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
