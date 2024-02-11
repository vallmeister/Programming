import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        adjacency_list = [[] for _ in range(n + 1)]
        for source, target, cost in roads:
            adjacency_list[source].append([target, cost])
            adjacency_list[target].append([source, cost])

        shortest_paths = [[] for _ in range(n + 1)]
        for root in range(1, n + 1):
            distances = [math.inf] * (n + 1)
            pq = [(0, root)]
            while pq:
                dist, node = heappop(pq)
                if dist < distances[node]:
                    distances[node] = dist
                    for neighbor, d in adjacency_list[node]:
                        heappush(pq, (dist + d, neighbor))
            shortest_paths[root] = distances

        ans = [math.inf] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                ans[i - 1] = min(ans[i - 1], (k + 1) * shortest_paths[i][j] + appleCost[j - 1])
        return ans


s = Solution()
print(s.minCost(n=4, roads=[[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]], appleCost=[56, 42, 102, 301], k=2))
