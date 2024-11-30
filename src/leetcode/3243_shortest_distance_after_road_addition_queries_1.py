from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)
        ans = []
        for u, v in queries:
            graph[u].append(v)
            ans.append(self.bfs(n, graph))
        return ans

    def bfs(self, n, graph):
        q = [(0, 0)]
        ans = n
        shortest_way = [n] * n
        while q:
            dist, node = heappop(q)
            if shortest_way[node] <= dist:
                continue
            shortest_way[node] = dist

            if node == n - 1:
                return dist
            for neighbor in graph[node]:
                heappush(q, (dist + 1, neighbor))
        return ans


s = Solution()
print(s.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))
