class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1 - obstacleGrid[m - 1][n - 1]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + dp[i][j + 1])
        return dp[0][0]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0], [0, 1]]))
print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
