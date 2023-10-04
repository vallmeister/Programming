from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited_rows = set()
        visited_columns = set()
        ans = []
        row = 0
        col = 0
        dr, dc = 0, 1
        for _ in range(m * n):
            ans.append(matrix[row][col])
            if dr == 0 and dc == 1 and (col + dc >= n or col + dc in visited_columns):
                visited_rows.add(row)
                dr, dc = 1, 0
            elif dr == 1 and dc == 0 and (row + dr >= m or row + dr in visited_rows):
                visited_columns.add(col)
                dr, dc = 0, -1
            elif dr == 0 and dc == -1 and (col + dc < 0 or col + dc in visited_columns):
                visited_rows.add(row)
                dr, dc = -1, 0
            elif dr == -1 and dc == 0 and (row + dr < 0 or row + dr in visited_rows):
                visited_columns.add(col)
                dr, dc = 0, 1
            row += dr
            col += dc
        return ans


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
