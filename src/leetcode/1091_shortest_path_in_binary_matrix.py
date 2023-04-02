class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        path = 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = [(0, 0)]
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        visited = {(0, 0)}

        while queue:
            next_queue = []
            for row, col in queue:
                if row == col == n - 1:
                    return path
                for d in directions:
                    next_row = row + d[0]
                    next_col = col + d[1]
                    if not (0 <= next_row < n and 0 <= next_col < n):
                        continue
                    if (next_row, next_col) in visited:
                        continue
                    if grid[next_row][next_col] != 0:
                        continue
                    visited.add((next_row, next_col))
                    next_queue.append((next_row, next_col))
            queue = next_queue
            path += 1

        return -1


s = Solution()
print(s.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]))
print(s.shortestPathBinaryMatrix([[0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]))
