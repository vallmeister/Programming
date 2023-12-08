from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for row in range(m):
            for col in range(n):
                live_neighbors = board[row][col]
                for dx, dy in directions:
                    neighbor_row = row + dx
                    neighbor_col = col + dy
                    if 0 <= neighbor_row < m and 0 <= neighbor_col < n and board[neighbor_row][neighbor_col] > 0:
                        live_neighbors += 1
                if board[row][col] == 0:
                    live_neighbors *= -1
                board[row][col] = live_neighbors
        for row in range(m):
            for col in range(n):
                if board[row][col] in {1, 2}:
                    board[row][col] = 0
                elif board[row][col] in {3, 4}:
                    board[row][col] = 1
                elif board[row][col] > 4:
                    board[row][col] = 0
                elif board[row][col] == -3:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


s = Solution()
matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
s.gameOfLife(matrix)
print(matrix)
matrix = [[1, 1], [1, 0]]
s.gameOfLife(matrix)
print(matrix)
matrix = [[1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0]]
s.gameOfLife(matrix)
print(matrix)
