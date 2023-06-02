from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            row, col, dist = q.popleft()
            if rooms[row][col] == -1:
                continue
            if rooms[row][col] == 2 ** 31 - 1:
                rooms[row][col] = dist
            for dr, dc in directions:
                if not (0 <= row + dr < m and 0 <= col + dc < n):
                    continue
                elif rooms[row + dr][col + dc] != 2 ** 31 - 1:
                    continue
                q.append((row + dr, col + dc, dist + 1))
