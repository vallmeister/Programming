from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def dynamic_programming(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


    def dynamic_programming_optimized(self, n):
        dp_0 = 1
        dp_1 = 1
        for i in range(2, n + 1):
            dp_1, dp_0 = dp_1 + dp_0, dp_1
        return dp_1


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(44))
