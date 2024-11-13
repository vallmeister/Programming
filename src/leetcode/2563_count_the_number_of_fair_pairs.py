import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            left = max(bisect.bisect_left(nums, lower - num), i + 1)
            right = min(bisect.bisect_right(nums, upper - num) - 1, len(nums) - 1)
            ans += max(0, right - left + 1)
        return ans


s = Solution()
print(s.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
