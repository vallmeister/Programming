class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 10 for _ in range(n + 1)]
        for i in range(10):
            dp[1][i] = 1
        for i in range(2, n + 1):
            dp[i][0] = dp[i - 1][4] + dp[i - 1][6]
            dp[i][1] = dp[i - 1][6] + dp[i - 1][8]
            dp[i][2] = dp[i - 1][7] + dp[i - 1][9]
            dp[i][3] = dp[i - 1][4] + dp[i - 1][8]
            dp[i][4] = dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][9]
            dp[i][6] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][7]
            dp[i][7] = dp[i - 1][2] + dp[i - 1][6]
            dp[i][8] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][9] = dp[i - 1][2] + dp[i - 1][4]
        return sum(dp[n][i] for i in range(10)) % MOD


s = Solution()
print(s.knightDialer(1))
print(s.knightDialer(2))
print(s.knightDialer(3131))
