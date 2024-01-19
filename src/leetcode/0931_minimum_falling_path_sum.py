class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        curr_row = matrix[n - 1]
        for i in range(n - 2, -1, -1):
            row = [0] * n
            for j in range(n):
                row[j] = matrix[i][j] + min(curr_row[max(j - 1, 0)], curr_row[j],
                                            curr_row[min(j + 1, n - 1)])
            curr_row = row
        return min(curr_row)


s = Solution()
print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(s.minFallingPathSum([[-19, 57], [-40, -5]]))
