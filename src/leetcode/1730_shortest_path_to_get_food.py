from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i, j, 0))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        while q:
            i, j, cost = q.popleft()
            if not 0 <= i < m or not 0 <= j < n or (i, j) in visited or grid[i][j] == 'X':
                continue
            elif grid[i][j] == '#':
                return cost
            visited.add((i, j))
            for di, dj in directions:
                q.append((i + di, j + dj, cost + 1))
        return -1
