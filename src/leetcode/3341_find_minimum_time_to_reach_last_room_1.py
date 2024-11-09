from heapq import heappop, heappush
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(moveTime)
        n = len(moveTime[0])
        q = [(0, 0, 0)]
        visited = set()
        while q:
            t, i, j = heappop(q)
            if i == m - 1 and j == n - 1:
                return t
            elif (i, j) in visited:
                continue
            visited.add((i, j))
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                heappush(q, (1 + max(t, moveTime[ni][nj]), ni, nj))
        return -1
