from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        components = [0] * n

        def dfs(node, visited):
            curr_value = values[node]
            for child in graph[node]:
                if child in visited:
                    continue
                visited.add(child)
                dfs(child, visited)
                curr_value += components[child]
            components[node] = curr_value

        dfs(0, {0})
        return sum(1 if comp % k == 0 else 0 for comp in components)


s = Solution()
print(s.maxKDivisibleComponents(5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6))
print(s.maxKDivisibleComponents(7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3))
