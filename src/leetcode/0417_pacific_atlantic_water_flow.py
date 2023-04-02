class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        pacific_reacher = []
        atlantic_reacher = []

        for i in range(m):
            pacific[i][0] = True
            pacific_reacher.append([i, 0])
            atlantic[i][n - 1] = True
            atlantic_reacher.append([i, n - 1])
        for j in range(n):
            pacific[0][j] = True
            pacific_reacher.append([0, j])
            atlantic[m - 1][j] = True
            atlantic_reacher.append([m - 1, j])

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            def bfs(queue, visited, ocean):
                while queue:
                    pos = queue.pop(0)
                    x, y = pos[0], pos[1]
                    visited[x][y] = True
                    for d in directions:
                        new_x = x + d[0]
                        new_y = y + d[1]
                        if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] \
                                and heights[new_x][new_y] >= heights[x][y] and not ocean[new_x][new_y]:
                            ocean[new_x][new_y] = True
                            queue.append([new_x, new_y])

            bfs(pacific_reacher, [[False] * n for _ in range(m)], pacific)
            bfs(atlantic_reacher, [[False] * n for _ in range(m)], atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result


s = Solution()
print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(s.pacificAtlantic([[1]]))
print(s.pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
print(s.pacificAtlantic([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
