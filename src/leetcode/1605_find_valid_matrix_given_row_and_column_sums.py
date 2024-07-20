from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0] * n for _ in range(m)]
        rowSum = [(-num, idx) for idx, num in enumerate(rowSum)]
        heapify(rowSum)
        colSum = [(-num, idx) for idx, num in enumerate(colSum)]
        heapify(colSum)

        while rowSum and colSum:
            row_num, row_idx = heappop(rowSum)
            col_num, col_idx = heappop(colSum)
            num = min(-row_num, -col_num)
            matrix[row_idx][col_idx] = num
            row_num += num
            col_num += num
            if row_num < 0:
                heappush(rowSum, (row_num, row_idx))
            if col_num < 0:
                heappush(colSum, (col_num, col_idx))
        return matrix


s = Solution()
print(s.restoreMatrix(rowSum=[3, 8], colSum=[4, 7]))
print(s.restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]))
