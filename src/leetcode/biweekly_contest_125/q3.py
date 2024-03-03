from collections import defaultdict, deque
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        adj = defaultdict(list)
        n = len(edges) + 1
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        paths = [defaultdict(list) for _ in range(n)]
        for i in range(n):
            q = deque()
            for idx, element in enumerate(adj[i]):
                neighbor, weight = element
                q.append((idx, neighbor, weight))
            visited = [False] * n
            visited[i] = True
            while q:
                idx, node, d = q.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                if d % signalSpeed == 0:
                    paths[i][idx].append(node)
                for neighbor, weight in adj[node]:
                    q.append((idx, neighbor, d + weight))

        ans = [0] * n
        for i in range(n):
            for k1, v1 in paths[i].items():
                for k2, v2 in paths[i].items():
                    if k1 >= k2:
                        continue
                    ans[i] += len(v1) * len(v2)
        return ans


s = Solution()
print(s.countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], signalSpeed=1))
print(
    s.countPairsOfConnectableServers([[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], signalSpeed=3))
print(
    s.countPairsOfConnectableServers([[1, 0, 2], [2, 1, 3], [3, 1, 3], [4, 1, 1], [5, 2, 3], [6, 1, 3], [7, 3, 2]], 3))
