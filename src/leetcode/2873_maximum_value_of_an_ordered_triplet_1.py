from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_i = max_diff = 0
        for k in range(n):
            num = nums[k]
            ans = max(ans, max_diff * num)
            max_diff = max(max_diff, max_i - num)
            max_i = max(max_i, num)
        return ans
