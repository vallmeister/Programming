import math
from functools import cache
from typing import List


class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def memo(prev, curr):
            if prev == curr == n:
                return 0
            elif curr >= n:
                return math.inf
            take = memo(prev, curr + 1)
            if self.get_gcd(nums[prev], nums[curr]) > 1:
                no_take = 1 + memo(curr + 1, curr + 1)
                return min(take, no_take)
            return take

        ans = memo(0, 0)
        return ans if ans < math.inf else -1

    def get_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a


s = Solution()
print(s.validSubarraySplit(nums=[2, 6, 3, 4, 3]))
print(s.validSubarraySplit(nums=[3, 5]))
print(s.validSubarraySplit(nums=[1, 2, 1]))
