class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        closed_islands = 0

        def dfs(row, col):
            grid[row][col] = 1
            if row == 0 or col == 0 or row == m - 1 or col == n - 1:
                if row > 0 and grid[row - 1][col] == 0:
                    dfs(row - 1, col)
                if col > 0 and grid[row][col - 1] == 0:
                    dfs(row, col - 1)
                if row < m - 1 and grid[row + 1][col] == 0:
                    dfs(row + 1, col)
                if col < n - 1 and grid[row][col + 1] == 0:
                    dfs(row, col + 1)
                return False
            is_island = True
            if grid[row - 1][col] == 0:
                is_island = is_island and dfs(row - 1, col)
            if grid[row][col - 1] == 0:
                is_island = is_island and dfs(row, col - 1)
            if grid[row + 1][col] == 0:
                is_island = is_island and dfs(row + 1, col)
            if grid[row][col + 1] == 0:
                is_island = is_island and dfs(row, col + 1)
            return is_island

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
