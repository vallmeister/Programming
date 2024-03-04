from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        @cache
        def memoization(i, j):
            if j >= n:
                return 1
            elif i >= m:
                return 0
            elif s[i] != t[j]:
                return memoization(i + 1, j)
            else:
                return memoization(i + 1, j) + memoization(i + 1, j + 1)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]
