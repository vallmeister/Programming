from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = [False] * m
        zero_columns = [False] * n

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows[row] = True
                    zero_columns[col] = True

        for row in range(m):
            for col in range(n):
                if zero_rows[row] or zero_columns[col]:
                    matrix[row][col] = 0


s = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s.setZeroes(matrix)
print(matrix)
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s.setZeroes(matrix)
print(matrix)
