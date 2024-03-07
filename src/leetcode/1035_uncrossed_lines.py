# Same logic as 1143 longest common subsequence
class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(1 + dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                ans = max(ans, dp[i][j])
        return ans


s = Solution()
print(s.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
print(s.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
