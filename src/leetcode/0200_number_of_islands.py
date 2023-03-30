class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(row, col):
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            if row > 0:
                dfs(row - 1, col)
            if col > 0:
                dfs(row, col - 1)
            if row < m - 1:
                dfs(row + 1, col)
            if col < n - 1:
                dfs(row, col + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)

        return islands


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
print(s.numIslands([["1", "1", "1"],
                    ["0", "1", "0"],
                    ["1", "1", "1"]]))
