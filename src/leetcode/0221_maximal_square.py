class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[max(i - 1, 0)][j], dp[max(i - 1, 0)][max(j - 1, 0)], dp[i][max(j - 1, 0)]) + 1
                    ans = max(ans, dp[i][j] * dp[i][j])
        return ans


s = Solution()
print(s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(s.maximalSquare([["0", "1"], ["1", "0"]]))
