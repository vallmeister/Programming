from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = defaultdict(int)
        h[0] = 1
        count = 0
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            count += h[curr_sum - k]
            h[curr_sum] += 1
        return count
