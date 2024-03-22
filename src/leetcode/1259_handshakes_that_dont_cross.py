class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10 ** 9 + 7
        n = numPeople // 2
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
                dp[i] %= MOD
        return dp[n]


s = Solution()
print(s.numberOfWays(4))
print(s.numberOfWays(6))
print(s.numberOfWays(8))
