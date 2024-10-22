from typing import List


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        directions = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
        board = [[-1] * n for _ in range(m)]
        board[r][c] = 0

        def backtracking(row, col, count):
            if count == m * n:
                return True
            for dr, dc in directions:
                if 0 <= row + dr < m and 0 <= col + dc < n and board[row + dr][col + dc] == -1:
                    board[row + dr][col + dc] = count
                    if backtracking(row + dr, col + dc, count + 1):
                        return True
                    board[row + dr][col + dc] = -1
            return False

        backtracking(r, c, 1)
        return board


s = Solution()
print(s.tourOfKnight(3, 4, 0, 0))
