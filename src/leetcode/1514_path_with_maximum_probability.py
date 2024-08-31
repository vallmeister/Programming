import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            u, v = edge
            p = succProb[i]
            if p == 0.0:
                continue
            nll = -math.log(p)
            graph[u].append([v, nll])
            graph[v].append([u, nll])
        sp = [math.inf] * n
        pq = []
        heappush(pq, [0, start_node])
        while pq:
            d, node = heappop(pq)
            if d >= sp[node]:
                continue
            sp[node] = d
            for neighbor, dd in graph[node]:
                heappush(pq, [d + dd, neighbor])
        return round(math.exp(-sp[end_node]), 5)


s = Solution()
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print(s.maxProbability(3, [[0, 1]], [0.5], 0, 2))
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.0, 0.00001], 0, 2))
