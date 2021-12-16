hpos = 0
depth = 0
aim = 0
with open("input.txt") as file:
    # line = file.readline()
    for line in file:
        [direction, units] = line.split()
        units = int(units)
        if direction == "forward":
            hpos += units
            depth += aim*units
        elif direction == "down":
            aim += units
        else: # up
            aim -= units
        # line = file.readline()

print(hpos*depth)
