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
                num = abs(matrix[i][j])
                ans += num
                min_so_far = min(min_so_far, num)
                if num < 0:
                    neg_count ^= 1
                has_zero = has_zero or num == 0
        if neg_count == 0 or has_zero:
            return ans
        return ans - 2 * min_so_far
