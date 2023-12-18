import math
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        fst_max = -math.inf
        snd_max = -math.inf
        fst_min = math.inf
        snd_min = math.inf
        for num in nums:
            if num > fst_max:
                fst_max, snd_max = num, fst_max
            elif num > snd_max:
                snd_max = num
            if num < fst_min:
                fst_min, snd_min = num, fst_min
            elif num < snd_min:
                snd_min = num
        return fst_max * snd_max - fst_min * snd_min


s = Solution()
print(s.maxProductDifference([5, 6, 2, 7, 4]))
print(s.maxProductDifference([4, 2, 5, 9, 7, 4, 8]))
