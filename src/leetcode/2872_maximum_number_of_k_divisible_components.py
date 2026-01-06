from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = self.get_graph(n, edges)
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            curr_sum = values[node]
            curr_comps = 0
            for child in g[node]:
                if visited[child]:
                    continue
                child_sum, child_comps = dfs(child)
                curr_sum += child_sum
                curr_comps += child_comps
            if curr_sum % k == 0:
                curr_comps += 1
            return curr_sum, curr_comps

        _, ans = dfs(0)
        return ans

    def get_graph(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g


s = Solution()
print(s.maxKDivisibleComponents(5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6))
print(s.maxKDivisibleComponents(7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3))
