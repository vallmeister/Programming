from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = -1
        for num in nums:
            target = num
            curr_streak = 1
            while target ** 2 in nums and target ** 2 <= 10 ** 5:
                curr_streak += 1
                ans = max(ans, curr_streak)
                target **= 2
        return ans
