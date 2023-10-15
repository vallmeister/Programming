from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        @cache
        def num_ways(i, remain):
            if i == remain == 0:
                return 1
            elif remain == 0:
                return 0
            elif i < 0 or i >= arrLen:
                return 0
            return num_ways(i - 1, remain - 1) + num_ways(i + 1, remain - 1) + num_ways(i, remain - 1)

        return num_ways(0, steps) % (10 ** 9 + 7)

    def num_ways_dp(self, steps, arr_len):
        arr_len = min(arr_len, steps)
        dp = [[0] * (steps + 1) for _ in range(arr_len + 1)]
        dp[0][0] = 1
        for i in range(1, steps + 1):
            dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
            for j in range(1, arr_len):
                dp[j][i] = dp[j - 1][i - 1] + dp[j][i - 1] + dp[j + 1][i - 1]
        return dp[0][steps] % (10 ** 9 + 7)

    def num_ways_dp_optimized(self, steps, arr_len):
        arr_len = min(arr_len, steps)
        dp = [0] * arr_len
        dp[0] = 1
        for _ in range(steps):
            next_dp = [0] * arr_len
            for curr in range(arr_len):
                next_dp[curr] = dp[curr]
                if curr > 0:
                    next_dp[curr] += dp[curr - 1]
                if curr < arr_len - 1:
                    next_dp[curr] += dp[curr + 1]
            dp = next_dp
        return dp[0] % (10 ** 9 + 7)


s = Solution()
print(s.numWays(3, 2))
print(s.numWays(2, 4))
print(s.numWays(4, 2))
print(s.numWays(27, 7))
print(s.num_ways_dp(3, 2))
print(s.num_ways_dp(2, 4))
print(s.num_ways_dp(4, 2))
print(s.num_ways_dp(27, 7))
print(s.num_ways_dp(430, 148488))
print(s.num_ways_dp_optimized(3, 2))
print(s.num_ways_dp_optimized(2, 4))
print(s.num_ways_dp_optimized(4, 2))
print(s.num_ways_dp_optimized(27, 7))
print(s.num_ways_dp_optimized(430, 148488))
