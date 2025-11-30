from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = self.get_graph(n, edges)
        visited = [False] * n

        def dfs(node):
            if visited[node]:
                return 0, 0
            visited[node] = True
            c, v = 0, values[node] % k
            for child in g[node]:
                cc, cv = dfs(child)
                c += cc
                v += cv
                v %= k
            c += 1 if v % k == 0 else 0
            return c, v

        return dfs(0)[0]

    def get_graph(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g


s = Solution()
print(s.maxKDivisibleComponents(5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6))
print(s.maxKDivisibleComponents(7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3))
