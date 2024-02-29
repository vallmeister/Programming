class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        prev = matrix[0]
        n = len(prev)
        for curr in matrix[1:]:
            for i in range(n):
                curr[i] += min(prev[max(0, i - 1)], prev[i], prev[min(i + 1, n - 1)])
            prev = curr
        return min(prev)


s = Solution()
print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(s.minFallingPathSum([[-19, 57], [-40, -5]]))
