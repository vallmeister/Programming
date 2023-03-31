class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        closed_islands = 0

        def dfs(row, col):
            is_closed = True
            grid[row][col] = 1
            if row == 0 or col == 0 or row == m - 1 or col == n - 1:
                is_closed = False
            # be careful with lazy evaluation here; either use is_closed & dfs or dfs and is_closed, otherwise it
            # will skip the dfs
            if row > 0 and grid[row - 1][col] == 0:
                is_closed = dfs(row - 1, col) and is_closed
            if col > 0 and grid[row][col - 1] == 0:
                is_closed = dfs(row, col - 1) and is_closed
            if row < m - 1 and grid[row + 1][col] == 0:
                is_closed = dfs(row + 1, col) and is_closed
            if col < n - 1 and grid[row][col + 1] == 0:
                is_closed = dfs(row, col + 1) and is_closed
            return is_closed

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    closed_islands += 1

        return closed_islands


s = Solution()
print(s.closedIsland(
    [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]]))
print(s.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(s.closedIsland([[1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1]]))
print(s.closedIsland([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                      [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                      [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                      [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                      [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))
