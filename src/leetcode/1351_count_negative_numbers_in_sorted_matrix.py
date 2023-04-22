class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negatives = 0
        for i in range(m):
            left = 0
            right = n - 1
            left_most_neg_idx = n
            while left <= right:
                mid = (left + right) // 2
                if grid[i][mid] < 0:
                    left_most_neg_idx = min(left_most_neg_idx, mid)
                    right = mid - 1
                elif grid[i][mid] >= 0:
                    left = mid + 1
            negatives += n - left_most_neg_idx
        return negatives


s = Solution()
print(s.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(s.countNegatives([[3, 2], [1, 0]]))
