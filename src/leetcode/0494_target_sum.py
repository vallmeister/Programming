from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dp(i, curr_sum):
            if i >= n:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            return dp(i + 1, curr_sum + nums[i]) + dp(i + 1, curr_sum - nums[i])

        return dp(0, 0)
