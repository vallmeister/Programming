from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        mod_count = defaultdict(int)
        mod_count[0] += 1
        for num in nums:
            total = (((total + num) % k) + k) % k
            ans += mod_count[total]
            mod_count[total] += 1
        return ans
