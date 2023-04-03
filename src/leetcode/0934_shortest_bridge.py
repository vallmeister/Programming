class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def island_dfs(row, col, isle):
            if grid[row][col] == 1:
                isle.add((row, col))
            for d in directions:
                next_row = row + d[0]
                next_col = col + d[1]
                if not (0 <= next_row < n and 0 <= next_col < n):
                    continue
                elif grid[next_row][next_col] != 1 or (next_row, next_col) in isle:
                    continue
                island_dfs(next_row, next_col, isle)

        def find_island():
            island = set()
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        island_dfs(i, j, island)
                        return island

        first_island = find_island()
        bridge = 0
        queue = list(first_island)
        while queue:
            next_queue = []
            for x, y in queue:
                for d in directions:
                    nx = x + d[0]
                    ny = y + d[1]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    elif (nx, ny) in first_island:
                        continue
                    elif grid[nx][ny] == 1:
                        return bridge
                    grid[nx][ny] = 1
                    first_island.add((nx, ny))
                    next_queue.append((nx, ny))
            bridge += 1
            queue = next_queue
        return -1


s = Solution()
print(s.shortestBridge([[0, 1], [1, 0]]))
print(s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
print(s.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
