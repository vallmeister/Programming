import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        distances = [[math.inf] * n for _ in range(m)]
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
                    nd = dist
                    if grid[ni][nj] > nd:
                        nd = grid[ni][nj] + ((grid[ni][nj] - dist) % 2)
                    heappush(q, (nd + 1, ni, nj))
        return -1
