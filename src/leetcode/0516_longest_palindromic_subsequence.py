class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ans = 0
        for i in reversed(range(n)):
            for j in range(n):
                if j < i:
                    continue
                elif i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                ans = max(ans, dp[i][j])
        return ans


sol = Solution()
print(sol.longestPalindromeSubseq('bbbab'))
print(sol.longestPalindromeSubseq('cbbd'))
