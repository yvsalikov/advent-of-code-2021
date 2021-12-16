# Day 5: Hydrothermal Venture
# https://adventofcode.com/2021/day/5


points = {} # vents counter. key - position, value - count
with open("input.txt") as file:
    for line in file:
        x1y1, x2y2 = line.rstrip().split(" -> ")
        x1, y1 = [int(xy) for xy in x1y1.split(",")]
        x2, y2 = [int(xy) for xy in x2y2.split(",")]
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                point = str(x1) + "," + str(y)
                if point in points:
                    points[point] += 1
                else:
                    points[point] = 1
        if y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                point = str(x) + "," + str(y1)
                if point in points:
                    points[point] += 1
                else:
                    points[point] = 1

count = 0
for k, v in points.items():
    if v > 1:
        count += 1

print(f"There are {count} points where at least two lines overlap.")
    
