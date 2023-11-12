from collections import deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        graph = [[] for _ in range(n)]
        routes = [set(elem) for elem in routes]
        for i in range(n):
            for j in range(i + 1, n):
                if routes[i] & routes[j]:
                    graph[i].append(j)
                    graph[j].append(i)
        q = deque()
        for bus, stops in enumerate(routes):
            if source in stops:
                q.append((bus, 1))
        visited = set()
        while q:
            bus, num = q.popleft()
            if target in routes[bus]:
                return num
            visited.add(bus)
            for next_bus in graph[bus]:
                if next_bus in visited:
                    continue
                q.append((next_bus, num + 1))

        return -1


s = Solution()
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], source=1, target=6))
print(s.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12))
print(s.numBusesToDestination([[1, 7], [3, 5]], 5, 5))
