from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        islands = self.get_number_of_islands(grid)
        if islands != 1:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m * n):
            row = i // n
            col = i % n
            if grid[row][col] == 1:
                grid[row][col] = 0
                islands = self.get_number_of_islands(grid)
                if islands != 1:
                    return 1
                grid[row][col] = 1
        return 2

    def get_number_of_islands(self, grid):
        m = len(grid)
        n = len(grid[0])
        total_squares = m * n
        root = list(range(total_squares))
        rank = total_squares * [1]

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    root[ry] = rx
                elif rank[rx] > rank[ry]:
                    root[rx] = ry
                else:
                    root[ry] = rx
                    rank[rx] += 1

        for i in range(total_squares):
            row = i // n
            col = i % n
            if row > 0 and grid[row][col] == grid[row - 1][col]:
                union(i, i - n)
            if col > 0 and grid[row][col] == grid[row][col - 1]:
                union(i, i - 1)

        islands = set()
        for i in range(total_squares):
            row = i // n
            col = i % n
            if grid[row][col] == 1:
                islands.add(find(i))

        return len(islands)


s = Solution()
print(s.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(s.minDays([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]))
print(s.minDays([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]]))
