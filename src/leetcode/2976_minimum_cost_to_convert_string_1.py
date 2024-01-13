import math
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = [[math.inf] * 26 for _ in range(26)]
        n = len(cost)
        for i in range(n):
            s, t, c = original[i], changed[i], cost[i]
            adj[ord(s) - ord('a')][ord(t) - ord('a')] = min(adj[ord(s) - ord('a')][ord(t) - ord('a')], c)

        # Floyd-Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        n = len(source)
        ans = 0
        for i in range(n):
            char_s, char_t = source[i], target[i]
            if char_s == char_t:
                continue
            c = adj[ord(char_s) - ord('a')][ord(char_t) - ord('a')]
            if c == math.inf:
                return -1
            ans += c
        return ans


sol = Solution()
print(sol.minimumCost("abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                      changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(sol.minimumCost("aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]))
print(sol.minimumCost("abcd", target="abce", original=["a"], changed=["e"], cost=[10000]))
