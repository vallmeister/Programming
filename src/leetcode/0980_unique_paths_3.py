from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        obstacles = 0
        start = (-1, -1)
        end = (-1, -1)

        def prepare():
            nonlocal obstacles
            nonlocal start
            nonlocal end
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == -1:
                        obstacles += 1
                    elif grid[i][j] == 1:
                        start = (i, j)
                    elif grid[i][j] == 2:
                        end = (i, j)

        prepare()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        paths = 0

        def dfs(row, col, visited):
            if (row, col) == end:
                if len(visited) == m * n - obstacles - 1:
                    nonlocal paths
                    paths += 1
                return
            visited.add((row, col))
            for dr, dc in directions:
                if (row + dr, col + dc) in visited:
                    continue
                elif row + dr < 0 or row + dr >= m or col + dc < 0 or col + dc >= n:
                    continue
                elif grid[row + dr][col + dc] in {0, 2}:
                    dfs(row + dr, col + dc, visited)
            visited.remove((row, col))

        sr, sc = start
        dfs(sr, sc, set())
        return paths


s = Solution()
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
print(s.uniquePathsIII([[0, 1], [2, 0]]))
