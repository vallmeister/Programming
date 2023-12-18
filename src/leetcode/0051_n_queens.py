from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def backtrack(row, columns, diagonals, anti_diagonals, board):
            if row == n:
                nonlocal ans
                ans.append(list(board))
                return
            for col in range(n):
                if col in columns or row - col in diagonals or row + col in anti_diagonals:
                    continue
                columns.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                curr_row = '.' * col + 'Q' + '.' * (n - col - 1)
                board.append(curr_row)
                backtrack(row + 1, columns, diagonals, anti_diagonals, board)
                board.pop()
                columns.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        backtrack(0, set(), set(), set(), [])
        return ans


s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(1))
