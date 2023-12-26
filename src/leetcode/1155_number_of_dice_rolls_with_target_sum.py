class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for t in range(1, target + 1):
            if t <= k:
                dp[1][t] = 1
        for die in range(2, n + 1):
            for t in range(target + 1):
                for i in range(max(0, t - k), t):
                    dp[die][t] += dp[die - 1][i]
                    dp[die][t] %= MOD
        return dp[n][target] % MOD


s = Solution()
print(s.numRollsToTarget(1, k=6, target=3))
print(s.numRollsToTarget(2, k=6, target=7))
print(s.numRollsToTarget(30, k=30, target=500))
