from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        counter = defaultdict(int)
        flip_mask = 0
        for i in range(n):
            flip_mask |= (1 << i)
        for i in range(m):
            bin_num = 0
            for j in range(n):
                bin_num |= ((1 << j) & (matrix[i][j] << j))
            counter[bin_num] += 1
            counter[bin_num ^ flip_mask] += 1
        return max(counter.values())


s = Solution()
print(s.maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
