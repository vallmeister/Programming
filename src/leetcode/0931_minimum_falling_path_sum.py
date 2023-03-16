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

    def min_falling_path_sum_dp(self, matrix):
        n = len(matrix)
        memo = [[0] * n for _ in range(n)]
        for i in range(n):
            memo[n - 1][i] = matrix[n - 1][i]
        for i in range(n - 2, -1, -1):
            for j in range(n):
                memo[i][j] = matrix[i][j] + min(memo[i + 1][max(j - 1, 0)], memo[i + 1][j],
                                                memo[i + 1][min(j + 1, n - 1)])
        return min(memo[0])


s = Solution()
print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(s.minFallingPathSum([[-19, 57], [-40, -5]]))
