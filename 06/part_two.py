# Day 6: Lanternfish
# https://adventofcode.com/2021/day/6


timers_dist = [0 for i in range(9)] # timer_dist[0] = lanternfishes with times 0, etc.
with open("input.txt") as file:
    school = [int(fish) for fish in file.readline().split(",")]

for t in school:
    timers_dist[t] += 1

days = 256
for day in range(1, days + 1):
    newborn = timers_dist[0]
    for i in range(8):
        timers_dist[i] = timers_dist[i + 1]
    timers_dist[8] = newborn
    timers_dist[6] += newborn
    # print(f"Day {day}: {timers_dist}")

fishes = 0
for n in timers_dist:
    fishes += n

print(f"There are {fishes} fishes after {days} days.")