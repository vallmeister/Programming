from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def is_magic_square(r, c):
            count = [0] * 16
            row_sums = [0] * 3
            col_sums = [0] * 3
            pos_diag = 0
            neg_diag = 0
            for magic_row in range(r - 2, r + 1):
                for magic_col in range(c - 2, c + 1):
                    num = grid[magic_row][magic_col]
                    if not 1 <= num <= 9:
                        return False
                    count[num] += 1
                    row_sums[r - magic_row] += num
                    col_sums[c - magic_col] += num
                    if r - magic_row == c - magic_col:
                        pos_diag += num
                    if r - magic_row + c - magic_col == 2:
                        neg_diag += num
            magic_nums = all(count[i] == 1 for i in range(1, 10))
            rows_eq = row_sums[0] == row_sums[1] == row_sums[2]
            cols_eq = col_sums[0] == col_sums[1] == col_sums[2]
            return magic_nums and rows_eq and cols_eq and pos_diag == neg_diag

        for row in range(rows):
            for col in range(cols):
                if row < 2 or col < 2:
                    continue
                elif not 1 <= grid[row][col] <= 9:
                    continue
                elif is_magic_square(row, col):
                    ans += 1

        return ans


s = Solution()
print(s.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
