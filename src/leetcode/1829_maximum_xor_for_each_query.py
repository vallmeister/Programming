from functools import reduce
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_k = 2 ** maximumBit - 1
        ps = reduce(lambda x, y: x ^ y, nums, 0)
        ans = []
        for i in reversed(range(len(nums))):
            ans.append(ps ^ max_k)
            ps ^= nums[i]
        return ans
