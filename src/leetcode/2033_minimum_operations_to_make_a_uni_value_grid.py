from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        r = grid[0][0] % x
        values = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != r:
                    return -1
                values.append(grid[i][j])
        values.sort()
        median = values[m * n // 2]
        return sum(abs(v - median) // x for v in values)


s = Solution()
print(s.minOperations(grid=[[2, 4], [6, 8]], x=2))
print(s.minOperations(grid=[[1, 5], [2, 3]], x=1))
print(s.minOperations(grid=[[1, 2], [3, 4]], x=2))
print(s.minOperations([[931, 128], [639, 712]], 73))
