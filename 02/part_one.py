hpos = 0
depth = 0
with open("input.txt") as file:
    # line = file.readline()
    for line in file:
        [direction, units] = line.split()
        units = int(units)
        if direction == "forward":
            hpos += units
        elif direction == "down":
            depth += units
        else:
            depth -= units
        # line = file.readline()

print(hpos*depth)
