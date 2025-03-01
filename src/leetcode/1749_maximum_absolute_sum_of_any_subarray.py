from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        total_min = curr_min = 0
        total_max = curr_max = 0
        for num in nums:
            curr_max = max(curr_max + num, num)
            total_max = max(total_max, curr_max)

            curr_min = min(curr_min + num, num)
            total_min = min(total_min, curr_min)
        return max(total_max, abs(total_min))


s = Solution()
print(s.maxAbsoluteSum([1, -3, 2, 3, -4]))
print(s.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
