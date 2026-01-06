from heapq import heappush, heappop
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0])
        heap = []
        ans = 0
        for i in range(m):
            heappush(heap, (values[i][n - 1], i, n - 1))
        for d in range(1, m * n + 1):
            v, i, j = heappop(heap)
            ans += d * v
            if j > 0:
                heappush(heap, (values[i][j - 1], i, j - 1))
        return ans
