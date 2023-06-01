import math
from collections import deque
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])
        distances = [[[math.inf, 'z']] * n for _ in range(m)]
        directions = ((0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u'))
        result = [math.inf, 'impossible']
        q = deque()
        q.append((ball[0], ball[1], 0, ''))
        while q:
            row, col, distance, instructions = q.popleft()
            if [row, col] == hole:
                if distance < result[0]:
                    result = [distance, instructions]
                elif distance == result[0]:
                    result[1] = min(result[1], instructions)
            for dr, dc, ins in directions:
                r = row
                c = col
                d = distance
                while 0 <= r + dr < m and 0 <= c + dc < n and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                    d += 1
                    if [r, c] == hole:
                        if d < result[0]:
                            result = [d, instructions + ins]
                        elif d == result[0]:
                            result[1] = min(result[1], instructions + ins)
                if 0 < d < distances[r][c][0]:
                    distances[r][c] = [d, instructions + ins]
                    q.append((r, c, d, instructions + ins))
                elif 0 < d == distances[r][c][0] and instructions + ins < distances[r][c][1]:
                    distances[r][c][1] = instructions + ins
                    q.append((r, c, d, instructions + ins))

        return result[1]


s = Solution()
print(s.findShortestWay([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                        ball=[4, 3], hole=[0, 1]))
print(s.findShortestWay([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                        ball=[4, 3], hole=[3, 0]))
print(s.findShortestWay([[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1]],
                        ball=[0, 4], hole=[3, 5]))
