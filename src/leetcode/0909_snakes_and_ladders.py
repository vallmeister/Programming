import math
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        q = deque()
        q.append((1, 0))
        while q:
            curr, moves = q.popleft()
            if curr == n * n:
                return moves
            elif curr in visited:
                continue
            visited.add(curr)
            for i in range(curr + 1, min(curr + 6, n * n) + 1):
                row = n - 1 - (i - 1) // n
                col = (i - 1) % n
                if ((i - 1) // n) % 2 == 1:
                    col = n - 1 - col
                nxt = board[row][col] if board[row][col] != -1 else i
                q.append((nxt, moves + 1))
        return -1


s = Solution()
print(s.snakesAndLadders(
    [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
     [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
print(s.snakesAndLadders([[-1, -1], [-1, 3]]))
print(s.snakesAndLadders(
    [[-1, -1, 19, 10, -1], [2, -1, -1, 6, -1], [-1, 17, -1, 19, -1], [25, -1, 20, -1, -1], [-1, -1, -1, -1, 15]]))
