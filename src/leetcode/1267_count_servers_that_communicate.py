from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        servers = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    servers.append((i, j))
        ns = len(servers)
        communicating = set()
        servers.sort()
        for i in range(1, ns):
            i1, j1 = servers[i - 1]
            i2, j2 = servers[i]
            if i1 == i2:
                communicating.add((i1, j1))
                communicating.add((i2, j2))
        servers.sort(key=lambda x: x[1])
        for j in range(1, ns):
            i1, j1 = servers[j - 1]
            i2, j2 = servers[j]
            if j1 == j2:
                communicating.add((i1, j1))
                communicating.add((i2, j2))
        return len(communicating)


s = Solution()
print(s.countServers([[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]))
