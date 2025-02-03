from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        lt = 0
        for i in range(n):
            if nums[i] < nums[i - 1]:
                lt += 1
        return lt <= 1
