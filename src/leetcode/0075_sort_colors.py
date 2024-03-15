from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for col in nums:
            colors[col] += 1
        i = 0
        for col, freq in enumerate(colors):
            while freq > 0:
                nums[i] = col
                freq -= 1
                i += 1
