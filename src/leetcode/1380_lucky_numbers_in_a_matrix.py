import math
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        min_row = [math.inf] * m
        max_col = [-math.inf] * n

        for row in range(m):
            for col in range(n):
                num = matrix[row][col]
                min_row[row] = min(min_row[row], num)
                max_col[col] = max(max_col[col], num)

        lucky_numbers = []
        for row in range(m):
            for col in range(n):
                num = matrix[row][col]
                if num == min_row[row] == max_col[col]:
                    lucky_numbers.append(num)
        return lucky_numbers
