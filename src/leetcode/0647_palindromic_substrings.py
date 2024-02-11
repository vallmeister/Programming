class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        ans = 0
        for i in reversed(range(n)):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                    ans += 1
                elif j < i:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans += 1
        return ans


sol = Solution()
print(sol.countSubstrings('abc'))
print(sol.countSubstrings('aaa'))
