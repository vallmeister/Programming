class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        ans = 0
        dp[0] = 1
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
            dp[i] %= MOD
            if low <= i <= high:
                ans += dp[i]
                ans %= MOD

        return ans % MOD


s = Solution()
print(s.countGoodStrings(3, 3, 1, 1))
print(s.countGoodStrings(2, 3, 1, 2))
print(s.countGoodStrings(50000, 100000, 2, 3))
