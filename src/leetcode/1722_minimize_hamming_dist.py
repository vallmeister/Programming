from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        g = self.get_graph(n, allowedSwaps)
        visited = [False] * n
        ans = 0
        for node in range(n):
            if visited[node]:
                continue
            indices = self.bfs(g, visited, node)
            source_elements = defaultdict(int)
            target_elements = defaultdict(int)
            for i in indices:
                source_elements[source[i]] += 1
                target_elements[target[i]] += 1
            for i in indices:
                num = target[i]
                if source_elements[num] > 0:
                    source_elements[num] -= 1
                else:
                    ans += 1

        return ans

    def get_graph(self, n, allowedSwaps):
        g = [[] for _ in range(n)]
        for u, v in allowedSwaps:
            g[u].append(v)
            g[v].append(u)
        return g

    def bfs(self, g, visited, start):
        q = deque([start])
        indices = []
        while q:
            node = q.popleft()
            if visited[node]:
                continue
            visited[node] = True
            indices.append(node)
            for child in g[node]:
                q.append(child)
        return indices


s = Solution()
print(s.minimumHammingDistance(source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]))
print(s.minimumHammingDistance(source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]))
print(s.minimumHammingDistance(source=[5, 1, 2, 4, 3], target=[1, 5, 4, 2, 3],
                               allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]]))
