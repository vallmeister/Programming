from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        last = nums[0]
        for i in range(1, len(nums)):
            increasing = increasing and last <= nums[i]
            decreasing = decreasing and last >= nums[i]
            last = nums[i]
        return increasing or decreasing


s = Solution()
print(s.isMonotonic([1, 2, 2, 3]))
print(s.isMonotonic([6, 5, 4, 4]))
print(s.isMonotonic([1, 3, 2]))
