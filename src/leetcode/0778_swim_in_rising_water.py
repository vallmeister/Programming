from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        ans = 0
        while q:
            elevation, i, j = heappop(q)
            if visited[i][j]:
                continue
            visited[i][j] = True
            ans = max(ans, elevation)
            if i == j == n - 1:
                return ans
            for di, dj in directions:
                if not 0 <= i + di < n or not 0 <= j + dj < n:
                    continue
                heappush(q, (grid[i + di][j + dj], i + di, j + dj))
        return ans


s = Solution()
print(s.swimInWater([[0, 2], [1, 3]]))
print(
    s.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
