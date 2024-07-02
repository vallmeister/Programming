import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fst = math.inf
        snd = math.inf
        for num in nums:
            if num <= fst:
                fst = num
            elif num <= snd:
                snd = num
            else:
                return True
        return False
