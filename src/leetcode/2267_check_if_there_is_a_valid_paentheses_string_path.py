from functools import cache
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @cache
        def memo(i, j, count):
            if i >= m or j >= n or count < 0:
                return False
            count += (1 if grid[i][j] == '(' else -1)
            if i == m - 1 and j == n - 1 and count == 0:
                return True
            return memo(i + 1, j, count) or memo(i, j + 1, count)

        return memo(0, 0, 0)

    def dynamic_programming(self, grid):
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(' or (m + n) % 2 == 0:
            return False
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0:
                    dp[i][j] |= dp[i][j - 1]
                if grid[i][j] == '(':
                    dp[i][j] <<= 1
                else:
                    dp[i][j] >>= 1
        return dp[m - 1][n - 1] & 1 == 1


s = Solution()
print(s.dynamic_programming([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]))
