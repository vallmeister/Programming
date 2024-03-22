from functools import cache


class Solution:

    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        dp = {}
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                predecessor = w[:i] + w[i + 1:]
                if predecessor in dp:
                    dp[w] = max(dp[w], 1 + dp[predecessor])
        return max(dp.values())


sol = Solution()
print(sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(sol.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(sol.longestStrChain(["abcd", "dbqca"]))
print(sol.longestStrChain(
    ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj", "ksqvsq",
     "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]))
