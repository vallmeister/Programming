from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        zeroes = 0
        curr = nums[0]
        for num in nums[1:]:
            if curr == 0:
                zeroes += 1
                curr = num
            else:
                curr &= num
        if curr == 0:
            zeroes += 1
        return max(1, zeroes)
