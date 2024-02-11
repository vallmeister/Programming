import math
from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def recursive(row, col1, col2):
            if row == m:
                return 0
            elif col1 < 0 or col2 < 0 or col1 >= n or col2 >= n:
                return -math.inf
            result = grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            result += max(recursive(row + 1, new_col1, new_col2)
                          for new_col1 in [col1 - 1, col1, col1 + 1]
                          for new_col2 in [col2 - 1, col2, col2 + 1])
            return result

        dp = [[[0] * n for _ in range(n)] for _ in range(m + 1)]
        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result = grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]
                    result += max(dp[row + 1][new_col1][new_col2]
                                  for new_col1 in [col1 - 1, col1, col1 + 1]
                                  for new_col2 in [col2 - 1, col2, col2 + 1]
                                  if 0 <= new_col1 < n
                                  and 0 <= new_col2 < n)
                    dp[row][col1][col2] = result

        return dp[0][0][n - 1]


s = Solution()
print(s.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
