from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        total_triangles = n * n * 4

        root = list(range(total_triangles))
        rank = [1] * total_triangles

        def find(x):
            if x == root[x]:
                return x
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

        for i in range(n * n):
            row = i // n
            col = i % n
            if grid[row][col] == ' ':
                union(4 * i, 4 * i + 1)
                union(4 * i, 4 * i + 2)
                union(4 * i, 4 * i + 3)
            elif grid[row][col] == '/':
                union(4 * i, 4 * i + 3)
                union(4 * i + 1, 4 * i + 2)
            elif grid[row][col] == '\\':
                union(4 * i, 4 * i + 1)
                union(4 * i + 2, 4 * i + 3)
            if row > 0:
                union(4 * i, 4 * (i - n) + 2)
            if col > 0:
                union(4 * i + 3, 4 * (i - 1) + 1)

        areas = set()
        for i in range(total_triangles):
            areas.add(find(i))
        return len(areas)


s = Solution()
print(s.regionsBySlashes([" /", "/ "]))
