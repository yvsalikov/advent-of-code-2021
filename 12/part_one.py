# Advent of Code 2021
# https://adventofcode.com/2021
# Day 12: Passage Pathing


class CaveNetwork:
    def __init__(self, filename: str) -> None:
        self.vertises = {}
        with (open(filename)) as file:
            for line in file:
                v1, v2 = line.rstrip().split("-")
                try:
                    self.vertises[v1].append(v2)
                except KeyError:
                    self.vertises[v1] = [v2]
                try:
                    self.vertises[v2].append(v1)
                except KeyError:
                    self.vertises[v2] = [v1]
        self.paths = []
    
    def depth_first_search(self, vertex: str, end_vertex: str, visited: list, path: str) -> None:
        if vertex.islower():
            visited.append(vertex)
        
        path += vertex
        if vertex == end_vertex:
            # print(path)
            self.paths.append(path)
            return
        path += ","
        
        for adjacent in self.vertises[vertex]:
            if adjacent not in visited:
                self.depth_first_search(adjacent, end_vertex, visited, path)
                if adjacent.islower():
                    visited.pop() # mark last cave unvisited

    def get_number_of_paths(self) -> int:
        self.depth_first_search("start", "end", [], "")
        # print(*self.paths, sep="\n")
        return len(self.paths)


if __name__ == '__main__':
    network = CaveNetwork("input.txt")
    print(network.get_number_of_paths())

