import math
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        min_dist = -1
        distances = [[math.inf] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        q.append((start[0], start[1], 0))
        while q:
            row, col, distance = q.popleft()
            if [row, col] == destination:
                min_dist = distance if min_dist == -1 else min(min_dist, distance)
            for dr, dc in directions:
                r = row
                c = col
                d = distance
                while 0 <= r + dr < m and 0 <= c + dc < n and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                    d += 1
                if d < distances[r][c]:
                    distances[r][c] = d
                    q.append((r, c, d))
        return min_dist


s = Solution()
print(s.shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                         start=[0, 4], destination=[4, 4]))
print(s.shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                         start=[0, 4], destination=[3, 2]))
print(s.shortestDistance([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                         start=[4, 3], destination=[0, 1]))
