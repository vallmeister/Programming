import math
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        prev_dp = [[-math.inf] * 2 for _ in range(n + 1)]
        for j in range(n + 1):
            prev_dp[j][int(True)] = 0

        for i in reversed(range(m)):
            dp = [[-math.inf] * 2 for _ in range(n + 1)]
            dp[n][int(True)] = 0
            for j in reversed(range(n)):
                dp[j][int(False)] = max(nums1[i] * nums2[j] + prev_dp[j + 1][int(True)], prev_dp[j][int(False)],
                                        dp[j + 1][int(False)])
                dp[j][int(True)] = max(nums1[i] * nums2[j] + prev_dp[j + 1][int(True)], prev_dp[j][int(True)],
                                       dp[j + 1][int(True)])
            prev_dp = dp
        return prev_dp[0][0]


s = Solution()
print(s.maxDotProduct([2, 1, -2, 5], nums2=[3, 0, -6]))
print(s.maxDotProduct([3, -2], nums2=[2, -6, 7]))
print(s.maxDotProduct([-1, -1], nums2=[1, 1]))
print(s.maxDotProduct([-3, -8, 3, -10, 1, 3, 9], [9, 2, 3, 7, -9, 1, -8, 5, -1, -1]))
