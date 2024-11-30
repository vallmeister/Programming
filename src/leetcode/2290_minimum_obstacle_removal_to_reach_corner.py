from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        distances = [[m * n] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = [(0, 0, 0)]
        while q:
            dist, i, j = heappop(q)
            if i == m - 1 and j == n - 1:
                return dist
            elif dist >= distances[i][j]:
                continue
            distances[i][j] = dist
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    heappush(q, (dist + grid[ni][nj], ni, nj))
        return -1
