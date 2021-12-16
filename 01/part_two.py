
tally = 0
with open("input.txt") as file:
    m1 = int(file.readline())
    m2 = int(file.readline())
    m3 = int(file.readline())
    line = file.readline()
    while line:
        m4 = int(line)
        if m2 + m3 + m4 > m1 + m2 + m3:
            tally += 1
        m1 = m2
        m2 = m3
        m3 = m4
        line = file.readline()

print(tally)
