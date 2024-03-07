from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2
        return max(dp.values())
