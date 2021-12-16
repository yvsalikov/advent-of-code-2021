# Advent of Code 2021
# https://adventofcode.com/2021
# Day 11: Dumbo Octopus


class DumboOctopusesShoal:
    def __init__(self, filename: str):
        self.octopuses = []
        with open(filename) as file:
            for line in file:
                self.octopuses.append([int(o) for o in line.rstrip()])
        self.size = len(self.octopuses)
        self.already_flashed = [[False for x in range(self.size)] for y in range(self.size)]
        self.flashes = 0
        # self.debugprint(self.octopuses)
    
    def simulate_n_steps(self, steps: int) -> None:
        for n in range(steps):
            # increase energy level for all octopuses
            for i in range(self.size):
                for j in range(self.size):
                    self.octopuses[i][j] += 1
            # flash ones with energy > 9 and increase neighbours' energy
            for i in range(self.size):
                for j in range(self.size):
                    if self.octopuses[i][j] > 9 and not self.already_flashed[i][j]:
                        self.flash_this_one_and_adjasent_neighbours(i, j)
            # set energy level of flashed octopuses to 0
            for i in range(self.size):
                for j in range(self.size):
                    if self.octopuses[i][j] > 9:
                        self.octopuses[i][j] = 0
                        self.already_flashed[i][j] = False
            # self.debugprint(self.octopuses)
    
    def flash_this_one_and_adjasent_neighbours(self, x: int, y: int) -> None:
        self.already_flashed[x][y] = True
        self.flashes += 1
        neighbours = [(dx, dy)
                        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                        if 0 <= x + dx < self.size and 0 <= y + dy < self.size]
        for dx, dy in neighbours:
            self.octopuses[x + dx][y + dy] += 1
            if self.octopuses[x + dx][y + dy] > 9 and not self.already_flashed[x + dx][y + dy]:
                self.flash_this_one_and_adjasent_neighbours(x + dx, y + dy)

    def get_flashes(self) -> int:
        return self.flashes
    
    def debugprint(self, data):
        for line in data:
            for o in line:
                print(f"{o:3}", end="")
            print()
        print()


octopuses = DumboOctopusesShoal("input.txt")
octopuses.simulate_n_steps(100)
print(octopuses.get_flashes())

