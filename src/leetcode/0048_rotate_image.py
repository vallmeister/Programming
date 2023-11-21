from pprint import pprint
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - i - 1][n - 1 - j]
                matrix[n - i - 1][n - 1 - j] = tmp


s = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(mat)
pprint(mat)
mat = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate(mat)
pprint(mat)
