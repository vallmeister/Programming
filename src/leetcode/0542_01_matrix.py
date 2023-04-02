import math


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        distances = [[0] * n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])

        dist = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            next_queue = []
            for x, y in queue:
                distances[x][y] = dist
                for d in directions:
                    nx = x + d[0]
                    ny = y + d[1]
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    elif mat[nx][ny] != 1:
                        continue
                    next_queue.append([nx, ny])
                    mat[nx][ny] = 0
            dist += 1
            queue = next_queue

        return distances

    def update_matrix_dp(self, mat: list[list[int]]):
        m = len(mat)
        n = len(mat[0])
        distances = [[math.inf] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    continue
                if i > 0:
                    distances[i][j] = min(distances[i][j], distances[i - 1][j] + 1)
                if j > 0:
                    distances[i][j] = min(distances[i][j], distances[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    continue
                if i < m - 1:
                    distances[i][j] = min(distances[i][j], distances[i + 1][j] + 1)
                if j < n - 1:
                    distances[i][j] = min(distances[i][j], distances[i][j + 1] + 1)
        return distances


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(s.update_matrix_dp([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.update_matrix_dp([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
