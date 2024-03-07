class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                ans = max(ans, dp[i][j])
        return ans


s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
print(s.longestCommonSubsequence('abc', 'abc'))
print(s.longestCommonSubsequence('abc', 'def'))
print(s.longestCommonSubsequence('bl', 'yby'))
