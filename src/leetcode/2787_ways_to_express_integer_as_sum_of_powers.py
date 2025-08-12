# Tough question
# TODO: Revisit
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            power = i ** x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= power:
                    dp[i][j] += dp[i - 1][j - power]
                dp[i][j] %= MOD

        return dp[n][n]



s = Solution()
print(s.numberOfWays(10, 2))
print(s.numberOfWays(4, 1))
print(s.numberOfWays(265, 1))
