class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    if s[i:].startswith(w):
                        dp[i + len(w)] = True
        return dp[n]


sol = Solution()
print(sol.wordBreak('leetcode', ['leet', 'code']))
print(sol.wordBreak('applepenapple', ['apple', 'pen']))
print(sol.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
