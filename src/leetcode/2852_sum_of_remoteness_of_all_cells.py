from collections import defaultdict
from typing import List


class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = list(range(n * n))
        component = defaultdict(int)
        total = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px
                component[px] += component[py]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                total += grid[i][j]
                curr = i * n + j
                component[curr] = grid[i][j]
                if i > 0 and grid[i - 1][j] != -1:
                    neighbor = (i - 1) * n + j
                    union(neighbor, curr)
                if j > 0 and grid[i][j - 1] != -1:
                    neighbor = i * n + j - 1
                    union(neighbor, curr)

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                curr = i * n + j
                par = find(curr)
                ans += total - component[par]
        return ans


s = Solution()
print(s.sumRemoteness([[-1, 1, -1], [5, -1, 4], [-1, 3, -1]]))
print(s.sumRemoteness([[-1, 3, 4], [-1, -1, -1], [3, -1, -1]]))
print(s.sumRemoteness([[1]]))
print(s.sumRemoteness([[5, 5, 1], [2, 3, 9], [3, 6, 3]]))
