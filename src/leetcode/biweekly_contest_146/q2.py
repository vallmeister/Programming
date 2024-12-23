from functools import cache
from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(i, j, xor):
            if i >= m or j >= n:
                return 0
            xor ^= grid[i][j]
            if i == m - 1 and j == n - 1:
                if xor == k:
                    return 1
                else:
                    return 0
            return (dfs(i + 1, j, xor) + dfs(i, j + 1, xor)) % MOD

        return dfs(0, 0, 0)
