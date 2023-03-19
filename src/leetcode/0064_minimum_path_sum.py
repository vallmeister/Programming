class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        return self.min_path_sum_dp(grid)

    def min_path_sum_dp(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1 and j < n - 1:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
                elif i < m - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif j < n - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
        return dp[0][0]

    def min_path_sum_memo(self, grid):
        m = len(grid)
        n = len(grid[0])
        memo = {(m - 1, n - 1): grid[m - 1][n - 1]}

        def min_path(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            result = grid[i][j]
            if i < m - 1 and j < n - 1:
                result += min(min_path(i + 1, j), min_path(i, j + 1))
            elif i < m - 1:
                result += min_path(i + 1, j)
            elif j < n - 1:
                result += min_path(i, j + 1)
            memo[(i, j)] = result
            return result

        return min_path(0, 0)


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
