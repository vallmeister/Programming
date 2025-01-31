from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        parent = [-1] * n
        q = deque([0])
        while q:
            node = q.popleft()
            visited[node] = True
            for neighbor in g[node]:
                if visited[neighbor]:
                    continue
                elif parent[neighbor] != -1 and parent[neighbor] != node:
                    return False
                parent[neighbor] = node
                q.append(neighbor)
        return all(visited)


s = Solution()
print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
