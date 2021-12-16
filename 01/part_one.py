tally = 0
with open("input.txt") as file:
    line = file.readline()
    prev = int(line) #previous depth measurement
    line = file.readline()
    while line:
        curr = int(line) #current depth measurement
        if curr > prev:
            tally = tally + 1
        prev = curr
        line = file.readline()

print(tally)
