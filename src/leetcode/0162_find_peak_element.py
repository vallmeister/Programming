from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        pass


s = Solution()
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
