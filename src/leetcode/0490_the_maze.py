from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        q = deque()
        for dr, dc in directions:
            if 0 <= start[0] + dr < m and 0 <= start[1] + dc < n and maze[start[0] + dr][start[1] + dc] == 0:
                q.append((start[0], start[1], dr, dc))
        while q:
            row, col, dr, dc = q.popleft()
            if (row, col) in visited and [row, col] != start:
                continue
            elif row < 0 or row >= m or col < 0 or col >= n or maze[row][col] == 1:
                continue
            visited.add((row, col))  # Cancels starting from start and going in all directions from there
            if [row, col] == destination:
                return True
            while 0 <= row + dr < m and 0 <= col + dc < n and maze[row + dr][col + dc] == 0:
                row += dr
                col += dc
            for ddr, ddc in directions:
                if 0 <= row + ddr < m and 0 <= col + ddc < n and maze[row + ddr][col + ddc] == 0 and (
                row + ddr, col + ddc) not in visited:
                    q.append((row, col, ddr, ddc))

        return False


s = Solution()
print(s.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
                destination=[4, 4]))
print(s.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
                destination=[3, 2]))
print(s.hasPath([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], start=[4, 3],
                destination=[0, 1]))
