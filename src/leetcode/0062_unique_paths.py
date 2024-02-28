import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = max(dp[i][j], dp[i + 1][j] + dp[i][j + 1])
        return dp[0][0]

    def unique_paths_combinatorical(self, m, n):
        return math.factorial((m + n - 2)) // math.factorial(m - 1) // math.factorial(n - 1)


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
