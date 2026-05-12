from collections import deque
from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row, col):
            q = deque([(row, col, -1, -1)])
            while q:
                ii, jj, pi, pj = q.popleft()
                if visited[ii][jj] > 1:
                    return True
                visited[ii][jj] += 1
                for di, dj in directions:
                    ni, nj = ii + di, jj + dj
                    if not 0 <= ni < m or not 0 <= nj < n:
                        continue
                    elif grid[ii][jj] != grid[ni][nj] or ni == pi and nj == pj:
                        continue
                    q.append((ni, nj, ii, jj))
            return False

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                elif bfs(i, j):
                    return True
        return False


s = Solution()
print(s.containsCycle(grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))
print(s.containsCycle(grid=[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))
print(s.containsCycle(grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))
