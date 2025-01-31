from collections import deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [set() for _ in range(n + 1)]
        edge_indices = {}
        for i, (u, v) in enumerate(edges):
            graph[u].add(v)
            graph[v].add(u)
            edge_indices[(u, v)] = i
            edge_indices[(v, u)] = i

        def bfs(visited_nodes, visited_edges):
            q = deque([1])
            while q:
                node = q.popleft()
                if visited_nodes[node]:
                    return False
                visited_nodes[node] = True
                for neighbor in graph[node]:
                    idx = edge_indices[(node, neighbor)]
                    if visited_edges[idx]:
                        continue
                    visited_edges[idx] = True
                    q.append(neighbor)
            return all(visited_nodes[1:])

        for i in reversed(range(n)):
            curr_edges = [False] * n
            curr_edges[i] = True
            if bfs([False] * (n + 1), curr_edges):
                return edges[i]
        return [-1, -1]


s = Solution()
print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
print(s.findRedundantConnection([[2, 7], [7, 8], [3, 6], [2, 5], [6, 8], [4, 8], [2, 8], [1, 8], [7, 10], [3, 9]]))
print(s.findRedundantConnection([[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]))
print(s.findRedundantConnection(
    [[16, 25], [7, 9], [3, 24], [10, 20], [15, 24], [2, 8], [19, 21], [2, 15], [13, 20], [5, 21], [7, 11], [6, 23],
     [7, 16], [1, 8], [17, 20], [4, 19], [11, 22], [5, 11], [1, 16], [14, 20], [1, 4], [22, 23], [12, 20], [15, 18],
     [12, 16]]))
