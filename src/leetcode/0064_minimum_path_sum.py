class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
                elif i > 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
