import bisect
from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        ps = self.get_prefix_sum(nums)
        prev = [0] * (n + 2)
        dp = [0] * (n + 1)
        i = 0
        for j, num in enumerate(nums, 1):
            i = max(i, prev[j])
            dp[j] = dp[i] + 1
            k = bisect.bisect_left(ps, 2 * ps[j] - ps[i])
            prev[k] = j
        return dp[n]

    def get_prefix_sum(self, nums):
        ps = [0]
        for num in nums:
            ps.append(ps[-1] + num)
        return ps


s = Solution()
print(s.findMaximumLength(nums=[5, 2, 2]))
print(s.findMaximumLength(nums=[1, 2, 3, 4]))
print(s.findMaximumLength(nums=[4, 3, 2, 6]))
print(s.findMaximumLength([980, 973, 229, 51, 594]))
print(s.findMaximumLength([272, 482, 115, 925, 983]))
