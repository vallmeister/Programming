import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:

        MAX_WEIGHT = int(2 * 10e9)
        ans = []

        adj = self.get_adjacency(n, edges)
        sp = self.dijkstra(n, adj, source)

        if sp[destination] < target:
            return ans
        elif sp[destination] == target:
            return list(map(lambda x: [x[0], x[1], x[2]] if x[2] > 0 else [x[0], x[1], MAX_WEIGHT], edges))

        adj = self.get_adjacency(n, edges, True)
        sp = self.dijkstra(n, adj, source)

        if sp[destination] > target:
            return ans

        # TODO: Finish

        return ans

    def get_adjacency(self, n, edges, modify=False):
        adj = [[] for _ in range(n)]
        for u, v, weight in edges:
            if modify and weight == -1:
                weight = 1
            adj[u].append((v, weight))
            adj[u].append((u, weight))
        return adj

    def dijkstra(self, n, adj, source):
        sp = [math.inf] * n
        pq = []
        heappush(pq, (0, source))
        while pq:
            d, node = heappop(pq)
            if d >= sp[node]:
                continue
            sp[node] = d
            for neighbor, dd in adj[node]:
                if dd == -1:
                    continue
                heappush(pq, (d + dd, neighbor))
        return sp


s = Solution()
print(s.modifiedGraphEdges(n=5, edges=[[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], source=0, destination=1,
                           target=5))
print(s.modifiedGraphEdges(n=3, edges=[[0, 1, -1], [0, 2, 5]], source=0, destination=2, target=6))
print(s.modifiedGraphEdges(n=3, edges=[[0, 1, 2], [1, 2, -1]], source=0, destination=1, target=2))
