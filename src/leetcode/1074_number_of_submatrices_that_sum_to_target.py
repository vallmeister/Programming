from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        count = 0
        for r1 in range(1, m + 1):
            for r2 in range(r1, m + 1):
                h = defaultdict(int)
                h[0] = 1
                for col in range(1, n + 1):
                    curr_sum = dp[r2][col] - dp[r1 - 1][col]
                    count += h[curr_sum - target]
                    h[curr_sum] += 1
        return count


s = Solution()
print(s.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
print(s.numSubmatrixSumTarget([[1, -1], [-1, 1]], target=0))
print(s.numSubmatrixSumTarget([[904]], target=0))
