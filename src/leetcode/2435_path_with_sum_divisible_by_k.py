from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if i + 1 < m:
                        num = grid[i+1][j]
                        dp[i+1][j][(r + num) % k] += dp[i][j][r]
                        dp[i + 1][j][(r + num) % k] %= MOD
                    if j + 1 < n:
                        num = grid[i][j+1]
                        dp[i][j+1][(r + num) % k] += dp[i][j][r]
                        dp[i][j + 1][(r + num) % k] %= MOD

        return dp[m - 1][n - 1][0]


s = Solution()
print(s.numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3))
print(s.numberOfPaths(grid=[[0, 0]], k=5))
print(s.numberOfPaths(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1))
