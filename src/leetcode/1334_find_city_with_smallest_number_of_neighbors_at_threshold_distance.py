import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjacency_list = [[] for _ in range(n)]
        for source, target, weight in edges:
            adjacency_list[source].append([target, weight])
            adjacency_list[target].append([source, weight])

        shortest_paths = [[math.inf] * n for _ in range(n)]
        for source in range(n):
            distances = [math.inf] * n
            pq = [(0, source)]
            while pq:
                d, node = heappop(pq)
                if d < distances[node]:
                    distances[node] = d
                    for neighbor, distance in adjacency_list[node]:
                        heappush(pq, (distance + d, neighbor))
            shortest_paths[source] = distances

        city, count = -1, n + 1
        for i in range(n):
            curr = 0
            for j in range(n):
                if shortest_paths[i][j] <= distanceThreshold:
                    curr += 1
            if curr <= count:
                city = i
                count = curr
        return city
