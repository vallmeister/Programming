import math
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        buildings = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.add((i, j))
        empty_lands = [[[0, 0] for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_distance = math.inf
        for b in buildings:
            q = deque()
            visited = set()
            q.append((b[0], b[1], 1))
            while q:
                x, y, distance = q.popleft()
                for dx, dy in directions:
                    if not (0 <= x + dx < m and 0 <= y + dy < n):
                        continue
                    elif grid[x + dx][y + dy] in {1, 2}:
                        continue
                    elif (x + dx, y + dy) in visited:
                        continue
                    visited.add((x + dx, y + dy))
                    empty_lands[x + dx][y + dy][0] += 1
                    empty_lands[x + dx][y + dy][1] += distance
                    q.append((x + dx, y + dy, distance + 1))
                    if empty_lands[x + dx][y + dy][0] == len(buildings):
                        min_distance = min(min_distance, empty_lands[x + dx][y + dy][1])
        return min_distance if min_distance != math.inf else -1


s = Solution()
print(s.shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(s.shortestDistance([[1, 0]]))
print(s.shortestDistance([[1]]))
print(s.shortestDistance(
    [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]))
print(s.shortestDistance(
    [[1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 1, 1, 0, 1],
     [1, 0, 1, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 1],
     [0, 1, 1, 1, 1, 1, 1, 0]]))
