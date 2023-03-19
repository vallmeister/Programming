import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.unique_paths_dp(m, n)

    def unique_paths_combinatorical(self, m, n):
        return math.factorial((m + n - 2)) // math.factorial(m - 1) // math.factorial(n - 1)

    def unique_paths_dp(self, m, n):
        dp = [[1] * n for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

        return dp[0][0]

    def unique_paths_memo(self, m: int, n: int) -> int:
        memo = {(m - 1, n - 1): 1}

        def unique_paths(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            res = 0
            if i == m - 1 or j == n - 1:
                return 1
            if i < m - 1:  # move down
                res += unique_paths(i + 1, j)
            if j < n - 1:  # move right
                res += unique_paths(i, j + 1)
            memo[(i, j)] = res
            return memo[(i, j)]

        return unique_paths(0, 0)


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
