from functools import cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        @cache
        def memo(i, j):
            if i >= m:
                return 0
            start = j
            end = n - 1 - (i - j)
            return max(multipliers[i] * nums[start] + memo(i + 1, start + 1),
                       multipliers[i] * nums[end] + memo(i + 1, start))

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if j > i:
                    continue
                start = j
                end = n - 1 - (i - j)
                dp[i][j] = max(multipliers[i] * nums[start] + dp[i + 1][j + 1],
                               multipliers[i] * nums[end] + dp[i + 1][j])

        return dp[0][0]


s = Solution()
print(s.maximumScore([1, 2, 3], multipliers=[3, 2, 1]))
print(s.maximumScore([-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
