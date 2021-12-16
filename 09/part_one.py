# Advent of Code 2021
# https://adventofcode.com/2021
# Day 9: Smoke Basin

floor_heights = []
with open("input.txt") as file:
    for line in file:
        floor_heights.append([int(h) for h in line.rstrip()])

risk_level = 0
rows = len(floor_heights)
cols = len(floor_heights[0])
for row in range(rows):
    for col in range(cols):
        neighbours = [floor_heights[row + r][col + c] 
                        for r, c in [(-1, 0), (+1, 0), (0, -1), (0, +1)]
                        if 0 <= row + r < rows and 0 <= col + c < cols]
        if all(n > floor_heights[row][col] for n in neighbours):
            # print(f"Low level {floor_heights[row][col]} at [{row}][{col}]")
            risk_level += (floor_heights[row][col] + 1)

print(f"Risk level is {risk_level}")
