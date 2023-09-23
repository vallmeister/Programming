class Solution:
    def is_predecessor(self, s, t):
        i, j, c = 0, 0, 0
        while j < len(t):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                c += 1
                j += 1
        return c == 1

    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=lambda x: len(x))
        n = len(words)
        descendants = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                w1 = words[i]
                w2 = words[j]
                if len(w1) - len(w2) == -1 and self.is_predecessor(w1, w2):
                    descendants[i].append(j)
        chain = 0
        visited = set()

        def dfs(v, depth):
            if v in visited:
                return
            visited.add(v)
            nonlocal chain
            chain = max(chain, depth)
            for node in descendants[v]:
                dfs(node, depth + 1)

        for i in range(n):
            dfs(i, 1)
        return chain

    def longest_str_chain(self, words: list[str]) -> int:
        dp = {}
        words.sort(key=len)
        chain = 0
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                successor = w[:i] + w[i + 1:]
                if successor in dp:
                    dp[w] = max(dp[w], dp[successor] + 1)
            chain = max(chain, dp[w])
        return chain


sol = Solution()
print(sol.longest_str_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(sol.longest_str_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(sol.longest_str_chain(["abcd", "dbqca"]))
print(sol.longest_str_chain(
    ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj", "ksqvsq",
     "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]))
