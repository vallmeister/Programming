import math
from functools import cache
from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1, 0)]

        @cache
        def memo(i, j, cost):
            if cost > k:
                return -math.inf
            elif i == m - 1 and j == n - 1:
                return grid[i][j]
            ans = []
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if ni >= m or nj >= n:
                    continue
                ans.append(memo(ni, nj, cost + (1 if grid[ni][nj] else 0)))
            return grid[i][j] + max(ans)

        res = max(-1, memo(0, 0, 0))
        memo.cache_clear()
        return res


s = Solution()
print(s.maxPathScore(grid=[[0, 1], [2, 0]], k=1))
print(s.maxPathScore(grid = [[0, 1],[1, 2]], k = 1))
