from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        score = 0
        i = 0
        n = len(nums)
        while i < n - 1:
            j = i + 1
            while j < n - 1 and nums[j] <= nums[i]:
                j += 1
            score += nums[i] * (j - i)
            i = j
        return score
