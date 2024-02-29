class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        prev_row = triangle[0]
        for curr_row in triangle[1:]:
            n = len(curr_row)
            for i in range(n):
                curr_row[i] += min(prev_row[min(i, n - 2)], prev_row[max(i - 1, 0)])
            prev_row = curr_row
        return min(prev_row)


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(s.minimumTotal([[-10]]))
