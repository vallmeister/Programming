from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]
        return ans


s = Solution()
print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.transpose([[1, 2, 3], [4, 5, 6]]))
