class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j] and j - i + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
