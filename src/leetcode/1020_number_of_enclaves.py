class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        enclaves = 0

        def dfs(row, col):
            is_closed = True
            grid[row][col] = 0
            area = 1
            if row == 0 or col == 0 or row == m - 1 or col == n - 1:
                is_closed = False
            if row > 0 and grid[row - 1][col] == 1:
                next_closed, next_area = dfs(row - 1, col)
                is_closed = next_closed and is_closed
                area += next_area
            if col > 0 and grid[row][col - 1] == 1:
                next_closed, next_area = dfs(row, col - 1)
                is_closed = next_closed and is_closed
                area += next_area
            if row < m - 1 and grid[row + 1][col] == 1:
                next_closed, next_area = dfs(row + 1, col)
                is_closed = next_closed and is_closed
                area += next_area
            if col < n - 1 and grid[row][col + 1] == 1:
                next_closed, next_area = dfs(row, col + 1)
                is_closed = next_closed and is_closed
                area += next_area
            return is_closed, area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    closed, ones = dfs(i, j)
                    if closed:
                        enclaves += ones

        return enclaves


s = Solution()
print(s.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(s.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
