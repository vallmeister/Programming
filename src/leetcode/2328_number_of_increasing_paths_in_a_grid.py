from heapq import heappush, heappop
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[1] * n for _ in range(m)]

        heap = []
        for i in range(m):
            for j in range(n):
                heappush(heap, (-grid[i][j], i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        while heap:
            val, i, j = heappop(heap)
            val = -val
            for di, dj in directions:
                if 0 <= i + di < m and 0 <= j + dj < n and val < grid[i + di][j + dj]:
                    dp[i][j] += dp[i + di][j + dj]
                    dp[i][j] %= MOD
            ans += dp[i][j]
            ans %= MOD
        return ans


s = Solution()
print(s.countPaths(grid=[[1, 1], [3, 4]]))
print(s.countPaths(grid=[[1], [2]]))
