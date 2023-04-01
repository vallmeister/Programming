class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        distance = -1
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            next_queue = []
            for (x, y) in queue:
                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        next_queue.append((new_x, new_y))
                        grid[new_x][new_y] = 1
            distance += 1
            queue = next_queue
        if distance == 0:
            distance = -1
        return distance


s = Solution()
print(s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
print(s.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(s.maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
print(s.maxDistance([[1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                     [0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                     [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]]))
