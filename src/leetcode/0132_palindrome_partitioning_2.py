class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(n):
                is_palindrome[i][j] = j <= i or s[i] == s[j] and is_palindrome[i + 1][j - 1]

        dp = [n + 1] * (n + 1)
        dp[-1] = -1
        for i in reversed(range(n)):
            for j in range(i, n):
                if is_palindrome[i][j]:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
        return dp[0]


sol = Solution()
print(sol.minCut('aab'))
print(sol.minCut('a'))
print(sol.minCut('ab'))
print(
    sol.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))
