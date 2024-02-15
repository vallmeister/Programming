import math
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in reversed(range(2, n)):
            if nums[i] < prefix[i]:
                return prefix[i] + nums[i]
        return -1


s = Solution()
print(s.largestPerimeter([5, 5, 5]))
print(s.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))
print(s.largestPerimeter([5, 5, 50]))
