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
            if i == m - 1 and j == n - 1:
                return count == 0
            elif count < 0:
                return False
            ans = False
            if i < m - 1:
                value = (1 if grid[i + 1][j] == '(' else -1)
                ans = ans or memo(i + 1, j, count + value)
            if j < n - 1:
                value = (1 if grid[i][j + 1] == '(' else -1)
                ans = ans or memo(i, j + 1, count + value)
            return ans

        return memo(0, 0, 1)
