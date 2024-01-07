from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        j = 1
        while j < len(nums) and nums[j] == nums[j - 1] + 1:
            prefix += nums[j]
            j += 1
        while prefix in nums:
            prefix += 1
        return prefix


s = Solution()
print(s.missingInteger([1, 2, 3, 2, 5]))
print(s.missingInteger([3, 4, 5, 1, 12, 14, 13]))
print(s.missingInteger([14, 9, 6, 9, 7, 9, 10, 4, 9, 9, 4, 4]))
