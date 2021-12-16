# There must be more convinient way to do this
n = 12 # by hand
counts = [0 for i in range(n + 1)]
with open("input.txt") as file:
    for line in file:
        m = int(line, 2) # measure
        for i in range(n):
            if m & (1 << i):
                counts[i] += 1
        counts[n] += 1; # total counter

# print(counts)
mean = counts[n] / 2
gamma = 0
for i in range(n):
    if counts[i] > mean:
        gamma += (1 << i)

epsilon = 0b111111111111 - gamma
print(f"gamma = {gamma}, epsilon = {epsilon}")
print(f"power consumption is {gamma * epsilon}")
