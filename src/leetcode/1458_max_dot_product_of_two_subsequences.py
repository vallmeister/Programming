from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = nums1[0] * nums2[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], nums1[0] * nums2[i])
        for i in range(1, m):
            dp[i][0] = max(dp[i - 1][0], nums1[i] * nums2[0])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + nums1[i] * nums2[j], nums1[i] * nums2[j])
        print(dp)
        return dp[m - 1][n - 1]


s = Solution()
print(s.maxDotProduct([2, 1, -2, 5], nums2=[3, 0, -6]))
print(s.maxDotProduct([3, -2], nums2=[2, -6, 7]))
print(s.maxDotProduct([-1, -1], nums2=[1, 1]))
print(s.maxDotProduct([-3, -8, 3, -10, 1, 3, 9], [9, 2, 3, 7, -9, 1, -8, 5, -1, -1]))
