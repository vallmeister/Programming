from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n - i - 1]
        if n % 2 == 1:
            ans -= mat[n // 2][n // 2]
        return ans


s = Solution()
print(s.diagonalSum([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))
print(s.diagonalSum([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]]))
print(s.diagonalSum([[5]]))
