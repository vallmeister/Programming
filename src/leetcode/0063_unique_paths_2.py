class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        return self.unique_paths_without_obstacles_dp(obstacleGrid)

    def unique_paths_without_obstacles_dp(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 0 and dp[i + 1][n - 1] == 1:
                dp[i][n - 1] = 1
        for j in range(n - 2, -1, -1):
            if obstacleGrid[m - 1][j] == 0 and dp[m - 1][j + 1] == 1:
                dp[m - 1][j] = 1
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

    def unique_paths_without_obstacles_memo(self, grid):
        if grid[0][0] == 1:
            return 0
        m = len(grid)
        n = len(grid[0])
        memo = {(m - 1, n - 1): 1 - grid[m - 1][n - 1]}

        def unique_paths(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            result = 0
            if i < m - 1 and grid[i + 1][j] == 0:
                result += unique_paths(i + 1, j)
            if j < n - 1 and grid[i][j + 1] == 0:
                result += unique_paths(i, j + 1)
            memo[(i, j)] = result
            return result

        return unique_paths(0, 0)


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0], [0, 1]]))
print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
