from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        min_streak = max_streak = ans = 1
        for num in nums[1:]:
            if num > prev:
                max_streak += 1
                min_streak = 1
            elif num < prev:
                max_streak = 1
                min_streak += 1
            else:
                min_streak = max_streak = 1
            ans = max(ans, min_streak, max_streak)
            prev = num
        return ans
