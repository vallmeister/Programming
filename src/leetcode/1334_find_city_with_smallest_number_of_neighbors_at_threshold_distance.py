import math
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[math.inf] * n for _ in range(n)]
        for source, target, weight in edges:
            graph[source][target] = weight
            graph[target][source] = weight
        for i in range(n):
            graph[i][i] = 0

        # all nodes shortest paths with Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        least_neighbors = math.inf
        city = -1
        for i in range(n - 1, -1, -1):
            reachable_neighbors = sum(1 if distance <= distanceThreshold else 0 for distance in graph[i])
            if reachable_neighbors < least_neighbors:
                least_neighbors = reachable_neighbors
                city = i
        return city


s = Solution()
print(s.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))
print(s.findTheCity(6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20))
