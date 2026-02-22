import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = math.inf
        n = len(nums)
        for i in range(n - k + 1):
            mn = nums[i]
            mx = nums[i + k - 1]
            ans = min(ans, mx - mn)
        return ans
