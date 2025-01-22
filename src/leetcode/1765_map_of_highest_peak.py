from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j, 0))

        result = [[0] * n for _ in range(m)]
        while q:
            i, j, height = q.popleft()
            if not 0 <= i < m or not 0 <= j < n or visited[i][j]:
                continue
            visited[i][j] = True
            result[i][j] = height
            for di, dj in directions:
                q.append((i + di, j + dj, height + 1))
        return result


s = Solution()
print(s.highestPeak([[0, 1], [0, 0]]))
