from functools import cache


class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def memoization(i, j):
            if i >= j:
                return 0
            elif s[i] == s[j]:
                return memoization(i + 1, j - 1)
            return 1 + min(memoization(i + 1, j), memoization(i, j - 1))

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(n):
                if i >= j:
                    continue
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

