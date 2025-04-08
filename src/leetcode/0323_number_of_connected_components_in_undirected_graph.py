from collections import deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))

        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)
            if parent_a == parent_b:
                return
            parents[parent_a] = parent_b

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        for u, v in edges:
            union(u, v)

        for i in range(n):
            find(i)

        return len(set(parents))

    def count_components_bfs(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i]:
                continue
            ans += 1
            q = deque([i])
            while q:
                node = q.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                for neighbor in g[node]:
                    q.append(neighbor)
        return ans


s = Solution()
print(s.countComponents(5, edges=[[0, 1], [1, 2], [3, 4]]))
print(s.countComponents(5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
