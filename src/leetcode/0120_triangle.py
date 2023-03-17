class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        curr_row = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            row = triangle[i]
            for j in range(len(row)):
                row[j] += min(curr_row[j], curr_row[j + 1])
            curr_row = row
        return triangle[0][0]


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(s.minimumTotal([[-10]]))
