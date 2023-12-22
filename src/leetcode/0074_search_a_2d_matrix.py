class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # search row
        top = 0
        bottom = m - 1
        row = None
        while top <= bottom:
            mid = (top + bottom) // 2
            curr_row = matrix[mid]
            if curr_row[0] <= target <= curr_row[-1]:
                row = curr_row
                break
            elif target < curr_row[0]:
                bottom = mid - 1
            elif curr_row[-1] < target:
                top = mid + 1
        if not row:
            return False
        # search target
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(s.searchMatrix([[1, 1]], 2))
