import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, c in roads:
            adj[u].append([v, c])
            adj[v].append([u, c])

        MOD = 10 ** 9 + 7
        sp = [math.inf] * n
        paths = [0] * n
        paths[0] = 1
        q = [(0, 0)]
        while q:
            dist, node = heappop(q)
            if dist > sp[node]:
                continue
            for neighbor, cost in adj[node]:
                if dist + cost < sp[neighbor]:
                    sp[neighbor] = dist + cost
                    heappush(q, (dist + cost, neighbor))
                    paths[neighbor] = paths[node]
                elif dist + cost == sp[neighbor]:
                    paths[neighbor] += paths[node]
                    paths[neighbor] %= MOD
        return paths[-1]


s = Solution()
print(s.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                               [0, 4, 5], [4, 6, 2]]))
print(s.countPaths(n=2, roads=[[1, 0, 10]]))
