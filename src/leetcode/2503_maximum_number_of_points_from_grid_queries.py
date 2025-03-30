from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        memo = {}
        total = 0
        heap = [(grid[0][0], 0, 0)]
        for q in sorted(queries):
            while heap and heap[0][0] < q:
                val, i, j = heappop(heap)
                if visited[i][j]:
                    continue
                visited[i][j] = True
                total += 1
                for di, dj in directions:
                    if not 0 <= i + di < m or not 0 <= j + dj < n:
                        continue
                    heappush(heap, (grid[i + di][j + dj], i + di, j + dj))
            memo[q] = total

        return [memo[q] for q in queries]


s = Solution()
print(s.maxPoints(grid=[[1, 2, 3], [2, 5, 7], [3, 5, 1]], queries=[5, 6, 2]))
print(s.maxPoints(grid=[[5, 2, 1], [1, 1, 2]], queries=[3]))
