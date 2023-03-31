class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        def dfs_island(row, col):
            is_sub_island = True
            grid2[row][col] = 0
            if grid1[row][col] == 0:
                is_sub_island = False

            if row > 0 and grid2[row - 1][col] == 1:
                is_sub_island = dfs_island(row - 1, col) and is_sub_island
            if col > 0 and grid2[row][col - 1] == 1:
                is_sub_island = dfs_island(row, col - 1) and is_sub_island
            if row < m - 1 and grid2[row + 1][col] == 1:
                is_sub_island = dfs_island(row + 1, col) and is_sub_island
            if col < n - 1 and grid2[row][col + 1] == 1:
                is_sub_island = dfs_island(row, col + 1) and is_sub_island

            return is_sub_island

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs_island(i, j):
                    count += 1
        return count


s = Solution()
print(s.countSubIslands([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                        [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))
print(s.countSubIslands([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                        [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))
