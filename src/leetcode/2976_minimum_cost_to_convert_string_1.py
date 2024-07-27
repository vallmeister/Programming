import math
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[math.inf] * 26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for s, t, weight in zip(original, changed, cost):
            s, t = ord(s) - ord('a'), ord(t) - ord('a')
            graph[s][t] = min(graph[s][t], weight)

        # Floyd-Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        min_cost = 0
        for s, t in zip(source, target):
            s, t = ord(s) - ord('a'), ord(t) - ord('a')
            if graph[s][t] == math.inf:
                return -1
            min_cost += graph[s][t]
        return min_cost


sol = Solution()
print(sol.minimumCost("abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                      changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(sol.minimumCost("aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]))
print(sol.minimumCost("abcd", target="abce", original=["a"], changed=["e"], cost=[10000]))
