import math
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        memo = {}

        def min_cost(i, walls):
            if (i, walls) in memo:
                return memo[(i, walls)]
            if walls <= 0:
                memo[(i, walls)] = 0
                return memo[(i, walls)]
            elif i >= n:
                return math.inf
            memo[(i, walls)] = min(min_cost(i + 1, walls), cost[i] + min_cost(i + 1, walls - 1 - time[i]))
            return memo[(i, walls)]

        return min_cost(0, n)

    def paint_walls_dp(self, cost, time):
        n = len(cost)
        dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(n - 1, -1, -1):
            for j in range(n + 1):
                dp[i][j] = min(dp[i + 1][j], cost[i] + dp[i + 1][max(0, j - 1 - time[i])])
        return dp[0][n]

    def paint_walls_dp_space_optimized(self, cost, time):
        n = len(cost)
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(n - 1, -1, -1):
            next_dp = [0] * (n + 1)
            for j in range(n + 1):
                next_dp[j] = min(dp[j], cost[i] + dp[max(0, j - 1 - time[i])])
            dp = next_dp
        return dp[n]


s = Solution()
print(s.paintWalls([1, 2, 3, 2], time=[1, 2, 3, 2]))
print(s.paintWalls([2, 3, 4, 2], time=[1, 1, 1, 1]))
print(s.paintWalls(
    [937, 252, 716, 781, 319, 198, 273, 554, 140, 68, 694, 583, 1080, 16, 450, 229, 710, 1003, 1117, 1036, 398, 874,
     289, 664, 600, 588, 372, 1066, 375, 532, 984, 328, 1067, 746],
    [5, 3, 1, 3, 2, 1, 3, 3, 5, 3, 5, 5, 4, 1, 3, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 3, 3, 4, 1, 3, 4, 1, 1, 5]))
print(s.paint_walls_dp([1, 2, 3, 2], time=[1, 2, 3, 2]))
print(s.paint_walls_dp([2, 3, 4, 2], time=[1, 1, 1, 1]))
print(s.paint_walls_dp(
    [937, 252, 716, 781, 319, 198, 273, 554, 140, 68, 694, 583, 1080, 16, 450, 229, 710, 1003, 1117, 1036, 398, 874,
     289, 664, 600, 588, 372, 1066, 375, 532, 984, 328, 1067, 746],
    [5, 3, 1, 3, 2, 1, 3, 3, 5, 3, 5, 5, 4, 1, 3, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 3, 3, 4, 1, 3, 4, 1, 1, 5]))
print(s.paint_walls_dp_space_optimized([1, 2, 3, 2], time=[1, 2, 3, 2]))
print(s.paint_walls_dp_space_optimized([2, 3, 4, 2], time=[1, 1, 1, 1]))
print(s.paint_walls_dp_space_optimized(
    [937, 252, 716, 781, 319, 198, 273, 554, 140, 68, 694, 583, 1080, 16, 450, 229, 710, 1003, 1117, 1036, 398, 874,
     289, 664, 600, 588, 372, 1066, 375, 532, 984, 328, 1067, 746],
    [5, 3, 1, 3, 2, 1, 3, 3, 5, 3, 5, 5, 4, 1, 3, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 3, 3, 4, 1, 3, 4, 1, 1, 5]))
