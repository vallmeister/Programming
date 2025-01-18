import math
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = [[math.inf] * n for _ in range(m)]
        q = [(0, 0, 0)]
        while q:
            nq = []
            for i, j, cost in q:
                if not 0 <= i < m or not 0 <= j < n or costs[i][j] <= cost:
                    continue
                costs[i][j] = cost
                for idx, (di, dj) in enumerate(directions):
                    if idx + 1 == grid[i][j]:
                        nq.append((i + di, j + dj, cost))
                    else:
                        nq.append((i + di, j + dj, cost + 1))
            q = nq
        return costs[m - 1][n - 1]


s = Solution()
print(s.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))
print(s.minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))
print(s.minCost([[1, 2], [4, 3]]))
print(s.minCost([[1, 1, 3], [2, 2, 2], [4, 4, 1]]))
