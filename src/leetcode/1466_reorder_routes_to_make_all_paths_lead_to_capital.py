from collections import deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        neighbors = [[] for _ in range(n)]
        for u, v in connections:
            neighbors[u].append(v)
            neighbors[v].append(u)
        roads = {(u, v) for u, v in connections}
        q = deque()
        q.append(0)
        visited = {0}
        changed_roads = 0
        while q:
            town = q.popleft()
            for neighbor in neighbors[town]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if (town, neighbor) in roads:
                    changed_roads += 1
                q.append(neighbor)
        return changed_roads


s = Solution()
print(s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(s.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
print(s.minReorder(3, [[1, 0], [2, 0]]))
