from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def memoization(house):
            if house >= n:
                return 0
            return max(memoization(house + 1), nums[house] + memoization(house + 2))

        dp = [0] * (n + 1)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        def dp_space_optimized():
            if n == 1:
                return nums[0]
            dp_0, dp_1 = 0, nums[0]
            current = 0
            for house in range(1, n):
                current = max(dp_0 + nums[house], dp_1)
                dp_0, dp_1 = dp_1, current
            return current

        return dp[n - 1]


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
