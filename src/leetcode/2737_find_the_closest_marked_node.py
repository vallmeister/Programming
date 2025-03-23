import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        marked = set(marked)
        graph = [[math.inf] * n for _ in range(n)]
        for u, v, weight in edges:
            graph[u][v] = min(graph[u][v], weight)
        q = [(0, s)]
        visited = [False] * n
        while q:
            distance, node= heappop(q)
            if visited[node]:
                continue
            elif node in marked:
                return distance
            visited[node] = True
            for neighbor in range(n):
                d = graph[node][neighbor]
                if d < math.inf:
                    heappush(q, (distance + d, neighbor))
        return -1
