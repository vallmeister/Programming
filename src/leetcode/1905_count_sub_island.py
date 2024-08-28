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

    def count_sub_islands_dsu(self, grid1, grid2):
        m = len(grid1)
        n = len(grid1[0])
        root = list(range(m * n))
        rank = [1] * m * n
        is_sub_island = [True] * m * n

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if grid2[i][j] == 0:
                    is_sub_island[idx] = False
                    continue
                if i > 0 and grid2[i - 1][j] == 1:
                    union(idx, idx - n)
                if j > 0 and grid2[i][j - 1] == 1:
                    union(idx, idx - 1)

        for i in range(m * n):
            row = i // n
            col = i % n
            if grid2[row][col] == 0:
                continue
            root_i = find(i)
            if i != root_i:
                is_sub_island[i] = False
            if grid1[row][col] != 1:
                is_sub_island[root_i] = False

        return sum(1 if is_sub_island[i] else 0 for i in range(m * n))


s = Solution()
print(s.countSubIslands([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                        [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))
print(s.countSubIslands([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                        [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))
