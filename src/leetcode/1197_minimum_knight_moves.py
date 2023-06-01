from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = set()
        directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        q = deque()
        q.append((0, 0, 0))
        while q:
            row, col, dist = q.popleft()
            if row == x and col == y:
                return dist
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in directions:
                q.append((row + dr, col + dc, dist + 1))
        return -1


s = Solution()
print(s.minKnightMoves(2, 1))
print(s.minKnightMoves(5, 5))
print(s.minKnightMoves(1, 1))
