# Advent of Code 2021
# https://adventofcode.com/2021
# Day 19: Beacon Scanner

from collections import deque
import numpy as np

class MapOfBeacons:
    def __init__(self, filename: str):
        class ScannersGraph:
            # Unweighted graph
            def __init__(self, vertices: int):
                self.vertices = vertices
                self.adjacent = [[] for i in range(self.vertices)];
                
            def add_edge(self, from_vertex: int, to_vertex: int) -> None:
                self.adjacent[from_vertex].append(to_vertex);
                self.adjacent[to_vertex].append(from_vertex);
            
            def find_shortest_path(self, from_vertex: int, to_vertex: int) -> list:
                queue = deque()
                visited = [False for i in range(self.vertices)];
                previous_vertex = [None for i in range(self.vertices)];
                
                visited[from_vertex] = True
                queue.append(from_vertex)
                path_found = False
                while queue and not path_found:
                    vertex = queue.popleft()
                    for adjacent_vertex in self.adjacent[vertex]:
                        if not visited[adjacent_vertex]:
                            visited[adjacent_vertex] = True
                            previous_vertex[adjacent_vertex] = vertex
                            queue.append(adjacent_vertex)
                            if adjacent_vertex == to_vertex:
                                path_found = True
                                break
                reversed_path = []
                vertex = to_vertex
                while vertex != None:
                    reversed_path.append(vertex)
                    vertex = previous_vertex[vertex]
                return reversed_path
        
        scanned_beacons = []
        with open(filename) as file:
            count = 0
            for line in file:
                if "--" in line:
                    # scanner header
                    scanned_beacons.append([])
                elif line == "\n":
                    # next scanner
                    count += 1
                else:
                    # beacon tuples
                    beacon = tuple([int(coord) for coord in line.rstrip().split(",")])
                    scanned_beacons[count].append(beacon)
        
        common_beacons = [dict() for i in range(len(scanned_beacons))]
        # Compare all scanners pairwise
        # OPTIMISATION: cache distances
        graph = ScannersGraph(len(scanned_beacons))
        for i in range(len(scanned_beacons)):
            for j in range(i+1, len(scanned_beacons)):
                count_common_beacons = 0
                source = []
                target = []
                for b_i in range(len(scanned_beacons[i])):
                    if count_common_beacons == 4:
                        break
                    dist1 = self.distances_to_neighbours(scanned_beacons[i], b_i)
                    for b_j in range(len(scanned_beacons[j])):
                        dist2 = self.distances_to_neighbours(scanned_beacons[j], b_j)
                        if self.count_identical_distances(dist1, dist2) >= 11:
                            graph.add_edge(i, j)
                            source.append(scanned_beacons[j][b_j])
                            target.append(scanned_beacons[i][b_i])
                            count_common_beacons += 1
                            if count_common_beacons == 4:
                                common_beacons[j][i] = source
                                common_beacons[i][j] = target
                                # print(f"Scanners #{i} and #{j} have overlapping cubes.")
                                # print(f"target: {target}")
                                # print(f"source: {source}")
                                break
        # print(common_beacons)
        # print()
        # self.transformation_matrices = {}
        # Add beacons detected by scanner #0
        self.beacons = set()
        self.scanners = []
        for beacon in scanned_beacons[0]:
            self.beacons.add(beacon)
        self.scanners.append((0, 0, 0))
        # Convert basis of beacons detected by other scanners
        for i in range(1, len(scanned_beacons)):
            path = graph.find_shortest_path(i, 0)
            # print(path)
            T = np.identity(4)
            for j in range(len(path) - 1):
                # 4 points are enough to compute transformations matrix
                target = common_beacons[path[j]][path[j + 1]]
                source = common_beacons[path[j + 1]][path[j]]
                T = np.dot(T, self.find_transformation_matrix(source, target))
                # print(f"{path[j + 1]} -> {path[j]}: {T}")
            for beacon in scanned_beacons[i]:
                self.beacons.add(self.transform(beacon, T))
            self.scanners.append(self.transform((0, 0, 0), T))
        
    def distances_to_neighbours(self, beacons: list, index: int) -> list:
        # squared distances
        distances = []
        for i in range(len(beacons)):
            if i == index:
                continue
            distance = ((beacons[i][0] - beacons[index][0])**2 +
                        (beacons[i][1] - beacons[index][1])**2 +
                        (beacons[i][2] - beacons[index][2])**2)
            distances.append(distance)
        return distances

    def count_identical_distances(self, dist1: list, dist2: list) -> int:
        # O(n^2)
        temp = [d for d in dist1 if d in dist2]
        return len(temp)
    
    def find_transformation_matrix(self, source: list, target: list):
        s = np.vstack((np.transpose(np.asarray(source)), [1,1,1,1]))
        t = np.vstack((np.transpose(np.asarray(target)), [1,1,1,1]))
        T = np.dot(t, np.linalg.inv(s))
        return T
    
    # def transform_to_base(self, index: int, point: tuple) -> tuple:
        # if not index:
            # return point
        # p = np.hstack((np.asarray(point), [1]))
        # i = index
        # while i:
            # print(f"{i} -> ", end="")
            # i, T = self.transformation_matrices[i]
            # p = np.dot(T, p)
        # print()
        # x, y, z = [int(i) for i in p[:-1]]
        # return tuple([round(i) for i in p[:-1]])
        
    def transform(self, beacon: tuple, matrix) -> tuple:
        p = np.dot(matrix, np.hstack((np.asarray(beacon), [1])))
        return tuple([round(i) for i in p[:-1]])
    
    def count_beacons(self) -> int:
        return len(self.beacons)
    
    def largest_distance(self) -> int:
        dist = []
        for i in range(len(self.scanners)):
            for j in range(i+1, len(self.scanners)):
                dist.append(abs(self.scanners[i][0] - self.scanners[j][0]) + 
                            abs(self.scanners[i][1] - self.scanners[j][1]) + 
                            abs(self.scanners[i][2] - self.scanners[j][2]))
        dist.sort()
        return dist[-1]

deepcave = MapOfBeacons("input.txt")
print(deepcave.count_beacons())
print(deepcave.largest_distance())
