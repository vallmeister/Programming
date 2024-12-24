from collections import deque
from typing import List



class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        g1 = self.get_adjacency_list(edges1)
        g2 = self.get_adjacency_list(edges2)

        dia1 = self.get_diameter(g1)
        dia2 = self.get_diameter(g2)

        return max(dia1, dia2, dia1 // 2 + dia1 % 2 + dia2 // 2 + dia2 % 2 + 1)

    def get_adjacency_list(self, edges):
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g

    def get_diameter(self, graph):
        _, farthest = self.bfs(graph, 0)
        diameter, _ = self.bfs(graph, farthest)
        return diameter

    def bfs(self, graph, start):
        max_d = farthest = -1
        q = deque()
        q.append((start, 0))
        visited = set()
        while q:
            node, d = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            if d > max_d:
                max_d = d
                farthest = node
            for child in graph[node]:
                q.appendleft((child, d + 1))
        return max_d, farthest
