class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            if row > 0:
                area += dfs(row - 1, col)
            if col > 0:
                area += dfs(row, col - 1)
            if row < m - 1:
                area += dfs(row + 1, col)
            if col < n - 1:
                area += dfs(row, col + 1)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area


s = Solution()
print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
print(s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
