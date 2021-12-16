# Advent of Code 2021
# https://adventofcode.com/2021
# Day 13: Transparent Origami


class TransparentOrigami:
    def __init__(self, filename: str) -> None:
        self.dots = []
        self.rules = []
        with (open(filename)) as file:
            # dots
            for line in file:
                if line == "\n":
                    break
                x, y = line.rstrip().split(",")
                self.dots.append((int(x), int(y)))
            # rules
            for line in file:
                axis, pos = line.rstrip().split("=")
                self.rules.append((axis[-1:], int(pos)))
    
    def fold_sheet(self, rule: tuple) -> None:
        (axis, position) = rule
        if axis == "x":
            for dot_x, dot_y in sorted(self.dots, key=lambda y: y[1]):
                if dot_x > position:
                    folded_dot = (2*position - dot_x, dot_y)
                    if folded_dot not in self.dots:
                        self.dots.insert(0, folded_dot)
                    self.dots.remove((dot_x, dot_y))
        else: # axis == y
            for dot_x, dot_y in sorted(self.dots, key=lambda y: y[1]):
                if dot_y > position:
                    folded_dot = (dot_x, 2*position - dot_y)
                    if folded_dot not in self.dots:
                        self.dots.insert(0, folded_dot)
                    self.dots.remove((dot_x, dot_y))
        # self.dots.sort(key=lambda y: y[1])
        # print(self.dots)

    def visible_dots_after_one_fold(self) -> int:
        self.fold_sheet(self.rules[0])
        return len(self.dots)
        
    def print_after_folding(self, filename: str) -> None:
        for rule in self.rules:
            self.fold_sheet(rule)
        max_x = 0
        max_y = 0
        for dot_x, dot_y in self.dots:
            if dot_x > max_x:
                max_x = dot_x
            if dot_y > max_y:
                max_y = dot_y
        lines = [[" " for x in range(max_x + 1)] for y in range(max_y + 1)]
        for dot_x, dot_y in self.dots:
            lines[dot_y][dot_x] = "#"
        with open(filename, "w") as file:
            for line in lines:
                file.write("".join(line) + "\n")


if __name__ == '__main__':
    origami = TransparentOrigami("input.txt")
    print(origami.visible_dots_after_one_fold())
    origami.print_after_folding("code.txt")
