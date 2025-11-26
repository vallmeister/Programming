import math
from typing import List


class Solution:
    """
    Revisit!!!
    """
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, -math.inf, -math.inf] for _ in range(n + 1)]
        for i in range(n):
            num = nums[i]
            r = num % 3
            for j in range(3):
                dp[i + 1][(j + r) % 3] = max(dp[i][(j + r) % 3], dp[i][j] + num)
        return dp[n][0]


s = Solution()
print(s.maxSumDivThree(nums=[3, 6, 5, 1, 8]))
print(s.maxSumDivThree(nums=[4]))
print(s.maxSumDivThree(nums=[1, 2, 3, 4, 4]))
