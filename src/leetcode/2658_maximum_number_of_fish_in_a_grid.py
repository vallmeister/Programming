from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]

        def bfs(row, col):
            if grid[row][col] == 0 or visited[row][col]:
                return 0
            fish = 0
            q = deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                if not 0 <= r < m or not 0 <= c < n or not grid[r][c] or visited[r][c]:
                    continue
                visited[r][c] = True
                fish += grid[r][c]
                for dr, dc in directions:
                    q.append((r + dr, c + dc))
            return fish

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, bfs(i, j))
        return ans
