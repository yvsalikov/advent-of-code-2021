# Day 5: Hydrothermal Venture
# https://adventofcode.com/2021/day/5


points = {} # vents counter. key - position, value - count
def inc_vents_count(key):
    if key in points:
        points[key] += 1
        # print(f"\t key {key} incremented")
    else:
        points[key] = 1
        # print(f"\t key {key} created")


with open("input.txt") as file:
    for line in file:
        x1y1, x2y2 = line.rstrip().split(" -> ")
        x1, y1 = [int(xy) for xy in x1y1.split(",")]
        x2, y2 = [int(xy) for xy in x2y2.split(",")]
        
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                inc_vents_count(str(x1) + "," + str(y))
        elif y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                inc_vents_count(str(x) + "," + str(y1))
        else:
            dx = x2 - x1
            if dx < 0:
                xsign = -1
            else:
                xsign = 1
            dy = y2 - y1
            if dy < 0:
                ysign = -1
            else:
                ysign = 1
            # dx = dy (45 degree)
            for r in range(abs(dx) + 1):
                inc_vents_count(str(x1 + xsign*r) + "," + str(y1 + ysign*r))

# print(points)
# print()

count = 0
for k, v in points.items():
    if v > 1:
        count += 1

print(f"There are {count} points where at least two lines overlap.")
