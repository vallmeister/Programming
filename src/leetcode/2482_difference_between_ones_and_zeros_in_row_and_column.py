from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        columns = [0] * n
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    rows[row] += 1
                    columns[col] += 1
                elif grid[row][col] == 0:
                    rows[row] -= 1
                    columns[col] -= 1
        ans = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                ans[row][col] = rows[row] + columns[col]
        return ans


s = Solution()
print(s.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
print(s.onesMinusZeros([[1, 1, 1], [1, 1, 1]]))
