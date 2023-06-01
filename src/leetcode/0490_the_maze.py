from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append(start)
        while q:
            row, col = q.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            if [row, col] == destination:
                return True
            for dr, dc in directions:
                r = row
                c = col
                while 0 <= r + dr < m and 0 <= c + dc < n and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                q.append((r, c))
        return False


s = Solution()
print(s.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
                destination=[4, 4]))
print(s.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
                destination=[3, 2]))
print(s.hasPath([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], start=[4, 3],
                destination=[0, 1]))
