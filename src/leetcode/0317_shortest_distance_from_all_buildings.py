import math
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        buildings = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        k = len(buildings)
        ans = math.inf

        reachable = [[0] * n for _ in range(m)]
        total_distance = [[0] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for bi, bj in buildings:
            visited = [[False] * n for _ in range(m)]
            q = deque([(bi, bj, 0)])
            while q:
                i, j, d = q.popleft()
                if visited[i][j]:
                    continue
                visited[i][j] = True
                reachable[i][j] += 1
                total_distance[i][j] += d
                if reachable[i][j] == k and grid[i][j] not in {1, 2}:
                    ans = min(ans, total_distance[i][j])
                for di, dj in directions:
                    if not 0 <= i + di < m or not 0 <= j + dj < n or grid[i + di][j + dj] in {1, 2}:
                        continue
                    q.append((i + di, j + dj, d + 1))
        return ans if ans < math.inf else -1


s = Solution()
print(s.shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(s.shortestDistance([[1, 0]]))
print(s.shortestDistance([[1]]))
print(s.shortestDistance([[1, 1], [0, 1]]))
print(s.shortestDistance(
    [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]))
