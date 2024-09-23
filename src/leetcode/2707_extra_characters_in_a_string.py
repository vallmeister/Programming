from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        @cache
        def memo(i):
            if i >= n:
                return 0
            tmp = [1 + memo(i + 1)]
            for word in dictionary:
                m = len(word)
                if s[i:].startswith(word):
                    tmp.append(memo(i + m))
            return min(tmp)

        return memo(0)

    def min_extra_char_dp(self, s, dictionary):
        n = len(s)
        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            dp[i] = dp[i + 1] + 1
            for word in dictionary:
                m = len(word)
                if s[i:].startswith(word):
                    dp[i] = min(dp[i], dp[i + m])
        return dp[0]

    def min_extra_char_trie(self, s, dictionary):
        trie = {}
        for word in dictionary:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['*'] = len(word)

        n = len(s)
        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            dp[i] = dp[i + 1] + 1
            curr = trie
            j = i
            while j < n and s[j] in curr:
                curr = curr[s[j]]
                if '*' in curr:
                    dp[i] = min(dp[i], dp[i + curr['*']])
                j += 1
        return dp[0]


sol = Solution()
print(sol.minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))
print(sol.minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]))
print(sol.min_extra_char_trie(s="leetscode", dictionary=["leet", "code", "leetcode"]))
