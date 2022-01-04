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
        
        self.beacons = set()
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
        self.transformation_matrices = {}
        # Add beacons detected by scanner #0
        for beacon in scanned_beacons[0]:
            self.beacons.add(beacon)
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
            # print(self.transform((0,0,0), T))
        
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
    
    def transform_to_base(self, index: int, point: tuple) -> tuple:
        if not index:
            return point
        p = np.hstack((np.asarray(point), [1]))
        i = index
        while i:
            # print(f"{i} -> ", end="")
            i, T = self.transformation_matrices[i]
            p = np.dot(T, p)
        # print()
        x, y, z = [int(i) for i in p[:-1]]
        return tuple([round(i) for i in p[:-1]])
        
    def transform(self, beacon: tuple, matrix) -> tuple:
        p = np.dot(matrix, np.hstack((np.asarray(beacon), [1])))
        return tuple([round(i) for i in p[:-1]])
    
    def count_beacons(self) -> int:
        return len(self.beacons)

deepcave = MapOfBeacons("input.txt")
print(deepcave.count_beacons())


# Beacon = namedtuple("Beacon", "x y z")

# def dist_to_others(beacons: list, index: int) -> list:
    # distances = []
    # for i in range(len(beacons)):
        # if i == index:
            # continue
        # distance = ((beacons[i].x - beacons[index].x)**2 +
                    # (beacons[i].y - beacons[index].y)**2 +
                    # (beacons[i].z - beacons[index].z)**2)
        # distances.append(distance)
    # return distances

# def intersection(list1: list, list2: list) -> list:
    # # O(n^2)
    # temp = [v for v in list1 if v in list2]
    # return temp

# scanners = []
# with open("input_test.txt") as file:
    # count = 0
    # for line in file:
        # if line == "\n":
            # count += 1
        # elif line[1] == "-":
            # scanners.append([])
        # else:
            # x, y, z = [int(coord) for coord in line.rstrip().split(",")]
            # scanners[count].append(Beacon(x, y, z))
    
# print(f"{len(scanners)} scanners")
# for beacons in scanners:
    # print(f"{len(beacons)} beacons.")


# for ib1 in range(len(scanners[0])):
    # dist1 = dist_to_others(scanners[0], ib1)
    # for ib2 in range(len(scanners[1])):
        # dist2 = dist_to_others(scanners[1], ib2)
        # if len(intersection(dist1, dist2)) >= 11:
            # print(f"({scanners[0][ib1].x}, {scanners[0][ib1].y}, {scanners[0][ib1].z}) -> ({scanners[1][ib2].x}, {scanners[1][ib2].y}, {scanners[1][ib2].z})")

# sc0_coords = np.array([[404, -588, -901],
                       # [528, -643, 409],
                       # [390, -675, -793],
                       # [-537, -823, -458]])
# sc0_coords = np.transpose(sc0_coords)
# sc0_coords = np.vstack((sc0_coords,[1,1,1,1]))

# sc1_coords = np.array([[-336, 658, 858],
                       # [-460, 603, -452],
                       # [-322, 571, 750],
                       # [605, 423, 415]])
# sc1_coords = np.transpose(sc1_coords)
# sc1_coords = np.vstack((sc1_coords,[1,1,1,1]))

# print(sc0_coords)
# print("->")
# print(sc1_coords)

# T = np.dot(sc0_coords, np.linalg.inv(sc1_coords))
# print(T)

# bsc1 = np.array([[-391], [539], [-444], [1]])
# print(bsc1)
# bsc0 = np.dot(T, bsc1)
# print("->")
# print(bsc0)


# bsc1 = np.array([[0], [0], [0], [1]])
# print(bsc1)
# bsc0 = np.dot(T, bsc1)
# print("->")
# print(bsc0)

# distances = []
# count = 0
# for beacons in scanners:
    # distances.append([])
    # for i, j in combinations(range(len(beacons)), 2):
        # distance = ((beacons[i].x - beacons[j].x)**2 +
                    # (beacons[i].y - beacons[j].y)**2 +
                    # (beacons[i].z - beacons[j].z)**2)
        # distances[count].append(distance)
    # # distances[count].sort()
    # count += 1
    # if count == 1:
        # break

# test1 = []
# j = 4
# print(scanners[0][j])
# for i in range(len(scanners[0])):
    # if i == j:
        # continue
    # distance = ((scanners[0][i].x - scanners[0][j].x)**2 +
                # (scanners[0][i].y - scanners[0][j].y)**2 +
                # (scanners[0][i].z - scanners[0][j].z)**2)
    # test1.append(distance)
    # # print(distance)
# print(len(test1))
# test2 = []
# k = 1
# print(scanners[1][0])
# for i in range(len(scanners[1])):
    # if i == k:
        # continue
    # distance = ((scanners[1][i].x - scanners[1][k].x)**2 +
                # (scanners[1][i].y - scanners[1][k].y)**2 +
                # (scanners[1][i].z - scanners[1][k].z)**2)
    # test2.append(distance)
    # # print(distance)
# print(len(test2))
# count = 1
# for t in test1:
    # if t in test2:
        # print(f"{count}: {t}")
        # count += 1
# print("---")
# count = 1
# for t in test2:
    # if t in test1:
        # print(f"{count}: {t}")
        # count += 1
# print("----------------")
# print(set(distances[0]) & set(distances[1]))

