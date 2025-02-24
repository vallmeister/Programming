import math
from collections import deque
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        parent = [-1] * n
        visited = [False] * n
        dist_alice = [math.inf] * n
        dist_bob = [math.inf] * n
        q = deque()
        q.append((0, 0))
        while q:
            node, d = q.popleft()
            visited[node] = True
            dist_alice[node] = d
            for child in tree[node]:
                if visited[child]:
                    continue
                parent[child] = node
                q.append((child, d + 1))

        d = 0
        while bob >= 0:
            dist_bob[bob] = d
            bob = parent[bob]
            d += 1

        visited = [False] * n

        def dfs(vertice):
            visited[vertice] = True
            if dist_alice[vertice] > dist_bob[vertice]:
                amount[vertice] = 0
            elif dist_alice[vertice] == dist_bob[vertice]:
                amount[vertice] //= 2
            paths = []
            for descendant in tree[vertice]:
                if visited[descendant]:
                    continue
                paths.append(dfs(descendant))
            if not paths:
                return amount[vertice]
            else:
                return max(paths) + amount[vertice]

        return dfs(0)


s = Solution()
print(s.mostProfitablePath(edges=[[0, 1], [1, 2], [1, 3], [3, 4]], bob=3, amount=[-2, 4, 2, -4, 6]))
print(s.mostProfitablePath(edges=[[0, 1]], bob=1, amount=[-7280, 2350]))
print(s.mostProfitablePath([[0, 1], [1, 2], [2, 3]], 3, [-5644, -6018, 1188, -8502]))
