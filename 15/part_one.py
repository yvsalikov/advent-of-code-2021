# Advent of Code 2021
# https://adventofcode.com/2021
# Day 15: Chiton


class Chiton:
    def __init__(self, filename) -> None:
        self.risk_levels = []
        with open(filename) as file:
            for line in file:
                self.risk_levels.append([int(l) for l in line.rstrip()])
        # self.fancyprint(self.risk_levels)
    
    def risk_of_shortest_path(self) -> int:
        h = len(self.risk_levels)
        w = len(self.risk_levels[0])
        total_risk = [[10*h*w for x in range(w)] for y in range(h)]
        total_risk[0][0] = 0
        # self.fancyprint(total_risk)
        visited = [[False for x in range(w)] for y in range(h)]
        visited[0][0] = True
        min_risk = []
        min_risk.append([0, 0, 0])
        while min_risk:
            min_risk.sort(key = lambda r: r[0])
            (least_risked, x, y) = min_risk.pop(0)
            neighbours = [(dx, dy)
                            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]
                            if 0 <= x + dx < w and 0 <= y + dy < h]
            for dx, dy in neighbours:
                if not visited[y + dy][x + dx]:
                    risk_on_path = least_risked + self.risk_levels[y + dy][x + dx]
                    if total_risk[y + dy][x + dx] > risk_on_path:
                        total_risk[y + dy][x + dx] = risk_on_path
                        new_least_risked = (total_risk[y + dy][x + dx], x + dx, y + dy)
                        min_risk.append(new_least_risked)
                        visited[y + dy][x + dx] = True
        # self.fancyprint(total_risk)
        return total_risk[h - 1][w - 1]
        
    # def fancyprint(self, totals: list) -> None:
        # for y in totals:
            # for x in y:
                # print(f"{x:2}", end="")
            # print()
        # print()

if __name__ == '__main__':
    
    cave = Chiton("input.txt")
    print(cave.risk_of_shortest_path())
    
    
