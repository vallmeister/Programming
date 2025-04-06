from functools import cache
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def memo(i, xor):
            if i >= n:
                return xor
            return memo(i + 1, xor) + memo(i + 1, xor ^ nums[i])

        return memo(0, 0)


s = Solution()
print(s.subsetXORSum([1, 3]))
print(s.subsetXORSum([5, 1, 6]))
