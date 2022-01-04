# Advent of Code 2021
# https://adventofcode.com/2021
# Day 20: Trench Map

# from functools import reduce
# from operator import add

class TrenchMap:
    def __init__(self, filename: str):
        self.image = []
        with open(filename) as file:
            self.algorithm = list(file.readline().rstrip())
            file.readline()
            for line in file:
                self.image.append(list(line.rstrip()))
        # self.algorithm = list(map(lambda x: 1 if x == "#" else 0, alg))
        self.infinite_pixels_lit = False
    
    def __str__(self) -> str:
        str_buff = []
        for line in self.image:
            str_buff.append("".join(line))
        return "\n".join(str_buff)
    
    def count_lit_pixels(self) -> int:
        if self.infinite_pixels_lit:
            return -1
        count = 0
        for line in self.image:
            count += line.count("#")
        return count

    def enhance(self, count: int = 1) -> None:
        for n in range(count):
            h = len(self.image)
            w = len(self.image[0])
            enhanced_image = [[" " for i in range(0, w + 2)] for j in range(0, h + 2)]
            if self.infinite_pixels_lit:
                mask = 0b111111111
                if self.algorithm[-1] == ".":
                    # All light pixels at infinity now dark
                    self.infinite_pixels_lit = False
            else:
                mask = 0b000000000
                if self.algorithm[0] == "#":
                    # All dark pixels at infinity now light
                    self.infinite_pixels_lit = True
            
            for y in range(0, h + 2):
                for x in range(0, w + 2):
                    index = mask
                    for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                        xi = x + dx - 1
                        yi = y + dy - 1
                        if 0 <= xi < w and 0 <= yi < h:
                            shift = 8 - ((dy + 1)*3 + (dx + 1))
                            if self.image[yi][xi] == "#":
                                index |= (1 << shift)
                            else: # "."
                                index &= ~(1 << shift)
                    enhanced_image[y][x] = self.algorithm[index]
            
            self.image = enhanced_image
    

trench = TrenchMap("input.txt")
# print(trench)
# print()
trench.enhance(50)
# print(trench)
print(trench.count_lit_pixels())

