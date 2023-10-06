from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        memo = {2: 2, 3: 3}

        def recursion(m):
            if m in memo:
                return memo[m]
            result = m
            for i in range(2, m // 2 + 1):
                result = max(result, recursion(i) * recursion(m - i))
            memo[m] = result
            return memo[m]

        return recursion(n)

    def integer_break_dp(self, n):
        if n == 2:
            return 1
        elif n == 3:
            return 2

        dp = [i for i in range(n + 1)]
        for i in range(4, n + 1):
            for j in range(2, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[n]


s = Solution()
print(s.integerBreak(2))  # 1
print(s.integerBreak(10))  # 36
print(s.integerBreak(13))  # 108
print(s.integerBreak(8))  # 18

print('dp solution')

print(s.integer_break_dp(2))  # 1
print(s.integer_break_dp(8))  # 1
print(s.integer_break_dp(10))  # 1
print(s.integer_break_dp(13))  # 1
