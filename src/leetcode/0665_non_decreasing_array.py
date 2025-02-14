import math
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        violations = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                violations += 1
        return violations <= 1


s = Solution()
print(s.checkPossibility([4, 2, 1]))
print(s.checkPossibility([3, 4, 2, 3]))
print(s.checkPossibility([5, 7, 1, 8]))
