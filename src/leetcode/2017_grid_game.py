from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        upper_ps = [0] * n
        lower_ps = [0] * n
        upper_ps[0] = grid[0][0]
        lower_ps[0] = grid[1][0]
        for i in range(n):
            upper_ps[i] = upper_ps[i - 1] + grid[0][i]
            lower_ps[i] = lower_ps[i - 1] + grid[1][i]
        ans = upper_ps[-1] - upper_ps[0]
        for i in range(1, n):
            ans = min(ans, max(upper_ps[-1] - upper_ps[i], lower_ps[i - 1]))
        return ans
