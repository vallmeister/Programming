import math
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        neg_count = 0
        has_zero = False
        ans = 0
        min_so_far = math.inf
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                ans += abs(num)
                min_so_far = min(min_so_far, abs(num))
                if num < 0:
                    neg_count += 1
                elif num == 0:
                    has_zero = True
        if neg_count % 2 == 0 or has_zero:
            return ans
        return ans - 2 * min_so_far
