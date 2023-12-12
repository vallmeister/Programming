from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = 0
        snd_num = 0
        for num in nums:
            if num > max_num:
                snd_num, max_num = max_num, num
            elif num > snd_num:
                snd_num = num
        return (max_num - 1) * (snd_num - 1)
