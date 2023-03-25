# Same logic as 1143 longest common subsequence
class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        return self.max_uncrossed_lines_dp(nums1, nums2)

    def max_uncrossed_lines_dp(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


s = Solution()
print(s.max_uncrossed_lines_dp([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
print(s.max_uncrossed_lines_dp([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
