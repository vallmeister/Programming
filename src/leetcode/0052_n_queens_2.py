import math


class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(row, columns, diagonals, anti_diagonals):
            if row == n:
                return 1
            solutions = 0
            for col in range(n):
                if col in columns or row - col in diagonals or row + col in anti_diagonals:
                    continue
                columns.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                solutions += backtrack(row + 1, columns, diagonals, anti_diagonals)
                columns.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
            return solutions

        return backtrack(0, set(), set(), set())


s = Solution()
print(s.totalNQueens(4))
print(s.totalNQueens(1))
print(s.totalNQueens(8))
