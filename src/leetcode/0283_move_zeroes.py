from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        j = 0
        while i < n and j < n:
            while i < n and nums[i] != 0:
                i += 1
            j = i + 1
            while j < n and nums[j] == 0:
                j += 1
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
