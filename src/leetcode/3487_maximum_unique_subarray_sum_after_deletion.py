import math
from functools import cache
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)

        @cache
        def memo(i, one_selected):
            if i >= n:
                if one_selected:
                    return 0
                else:
                    return -math.inf
            take = nums[i] + memo(i + 1, True)
            no_take = memo(i + 1, one_selected)
            return max(take, no_take)

        return memo(0, False)


s = Solution()
print(s.maxSum(nums=[1, 2, 3, 4, 5]))
print(s.maxSum([1, 1, 0, 1, 1]))
print(s.maxSum([1, 2, -1, -2, 1, 0, -1]))
