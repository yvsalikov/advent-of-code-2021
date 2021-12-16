# Advent of Code 2021
# https://adventofcode.com/2021
# Day 12: Passage Pathing


class CaveNetwork:
    def __init__(self, filename: str) -> None:
        self.vertices = {}
        with (open(filename)) as file:
            for line in file:
                v1, v2 = line.rstrip().split("-")
                try:
                    self.vertices[v1].append(v2)
                except KeyError:
                    self.vertices[v1] = [v2]
                try:
                    self.vertices[v2].append(v1)
                except KeyError:
                    self.vertices[v2] = [v1]
        # self.paths = []
        self.paths = set()
    
    def depth_first_search(self, vertex: str, end_vertex: str, visited: list, path: str) -> None:
        if vertex.islower():
            visited.append(vertex)
        
        # do not like this
        if "_" in vertex:
            path += vertex[:-1]
        else:
            path += vertex
        
        if vertex == end_vertex:
            # print(path)
            self.paths.add(path) # append(path)
            return
        path += ","
        
        for adjacent in self.vertices[vertex]:
            if adjacent not in visited:
                self.depth_first_search(adjacent, end_vertex, visited, path)
                if adjacent.islower():
                    visited.pop() # mark last cave unvisited

    def get_number_of_paths(self) -> int:
        self.paths.clear()
        self.depth_first_search("start", "end", [], "")
        return self.paths
    
    # do not like this
    # very ineffective
    def get_number_of_paths_twice(self) -> int:
        self.paths.clear()
        small_caves = [cave for cave in self.vertices if cave.islower()]
        small_caves.remove("start")
        small_caves.remove("end")
        
        for cave in small_caves:
            virtual_cave = cave + "_"
            self.vertices[virtual_cave] = []
            for v in self.vertices[cave]:
                self.vertices[v].append(virtual_cave)
                self.vertices[virtual_cave].append(v)
            self.depth_first_search("start", "end", [], "")
            for v in self.vertices[cave]:
                self.vertices[v].remove(virtual_cave)
            del self.vertices[virtual_cave]
        
        return self.paths


if __name__ == '__main__':
    network = CaveNetwork("input.txt")
    # p1 = network.get_number_of_paths()
    # print(*p1, sep="\n")
    # print(len(p1))
    p2 = network.get_number_of_paths_twice()
    # print(*p2, sep="\n")
    print(len(p2))

