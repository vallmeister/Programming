from functools import cache
from typing import List




class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m = len(words[0])
        n = len(target)
        frequencies = [[0] * 26 for _ in range(m)]
        for i in range(m):
            for word in words:
                letter = word[i]
                frequencies[i][ord(letter) - ord('a')] += 1
        
        @cache
        def dp(i, k):
            if i >= n:
                return 1
            elif k >= m:
                return 0
            letter = target[i]
            skip = dp(i, k + 1)
            take = frequencies[k][ord(letter) - ord('a')] * dp(i + 1, k + 1)
            return skip + take
        
        return dp(0, 0) % MOD


s = Solution()
print(s.numWays(words = ["acca","bbbb","caca"], target = "aba"))
print(s.numWays(["abba","baab"], target = "bab"))