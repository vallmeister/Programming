from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heights = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1:
                    heights[row][col] = 1
                    if row > 0:
                        heights[row][col] += heights[row - 1][col]
        ans = 0
        for i in range(m):
            row = heights[i]
            row.sort(reverse=True)
            for col in range(n):
                ans = max(ans, row[col] * (col + 1))
        return ans


s = Solution()
print(s.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(s.largestSubmatrix([[1, 0, 1, 0, 1]]))
print(s.largestSubmatrix([[1, 1, 0], [1, 0, 1]]))
print(s.largestSubmatrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]))
