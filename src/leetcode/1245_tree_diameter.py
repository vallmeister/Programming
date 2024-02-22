from collections import deque
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adjacency_list = [[] for _ in range(n)]
        for source, target in edges:
            adjacency_list[source].append(target)
            adjacency_list[target].append(source)

        def bfs(start):
            visited = set()
            q = deque()
            q.append((start, 0))
            target = max_dist = -1
            while q:
                node, distance = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if distance > max_dist:
                    target = node
                    max_dist = distance
                for neighbor in adjacency_list[node]:
                    q.append((neighbor, distance + 1))
            return target, max_dist

        b, _ = bfs(0)
        _, ans = bfs(b)
        return ans


s = Solution()
print(s.treeDiameter([[0, 1], [0, 2]]))
print(s.treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
