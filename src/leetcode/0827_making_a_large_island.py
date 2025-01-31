from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        root = list(range(n * n))
        rank = [1] * n * n
        size = [1] * n * n

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    root[rx] = ry
                    size[ry] += size[rx]
                elif rank[rx] > rank[ry]:
                    root[ry] = rx
                    size[rx] += size[ry]
                else:
                    root[ry] = rx
                    rank[rx] += 1
                    size[rx] += size[ry]

        def is_connected(x, y):
            return find(x) == find(y)

        for i in range(n * n):
            row, col = self.get_row_col(i, n)
            if grid[row][col] == 0:
                continue
            if row > 0 and grid[row - 1][col] == 1:
                union(i - n, i)
            if col > 0 and grid[row][col - 1] == 1:
                union(i - 1, i)

        ans = max(size)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(n * n):
            row, col = self.get_row_col(i, n)
            if grid[row][col]:
                continue
            islands = []
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not 0 <= nr < n or not 0 <= nc < n:
                    continue
                elif grid[nr][nc] == 0:
                    continue
                islands.append(self.get_index(nr, nc, n))
            curr_size = 1
            m = len(islands)
            for j in range(m):
                root_j = find(islands[j])
                curr_size += size[root_j]
                for k in range(j + 1, m):
                    if is_connected(islands[j], islands[k]):
                        root_k = find(islands[k])
                        curr_size -= size[root_k]
            ans = max(ans, curr_size)
        return ans

    def get_index(self, row, col, n):
        return row * n + col

    def get_row_col(self, index, n):
        return index // n, index % n


s = Solution()
print(s.largestIsland([[1, 0], [0, 1]]))
print(s.largestIsland([[1, 1], [1, 0]]))
print(s.largestIsland([[1, 1], [1, 1]]))
