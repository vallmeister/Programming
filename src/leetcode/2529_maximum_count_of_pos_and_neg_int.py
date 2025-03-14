import bisect
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg = bisect.bisect_right(nums, -1)
        pos = bisect.bisect_left(nums, 1)
        return max(neg, n - pos)
