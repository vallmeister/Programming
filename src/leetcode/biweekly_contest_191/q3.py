import math


class Solution:
    def minDays(self, n: int) -> int:
        max_streak = int(2 * math.sqrt(n))
        dp = [2 * n] * (n + 1)
        dp[0] = 0
        geometric_sums = [i * (i + 1) // 2 for i in range(1, max_streak + 1)]
        for i, geo_sum in enumerate(geometric_sums, start=1):
            if geo_sum > n:
                break
            dp[geo_sum] = i
        for i in range(1, n + 1):
            for j, geo_sum in enumerate(geometric_sums, start=1):
                if i + geo_sum > n:
                    break
                dp[i + geo_sum] = min(dp[i + geo_sum], dp[i] + 1 + j)
        return dp[n]


s = Solution()
print(s.minDays(2))
print(s.minDays(9))
print(s.minDays(12))
