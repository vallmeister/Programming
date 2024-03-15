from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        ps = defaultdict(int)
        cs = 0
        for num in nums:
            ps[cs] += 1
            cs += num
            ans += ps[cs - goal]
        return ans
