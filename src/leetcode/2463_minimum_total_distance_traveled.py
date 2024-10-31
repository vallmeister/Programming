import math
from functools import cache
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m = len(robot)
        n = len(factory)

        @cache
        def memo(i, j, curr_robots):
            if i >= m:
                return 0
            elif j >= n:
                return math.inf
            elif curr_robots >= factory[j][1]:
                return memo(i, j + 1, 0)
            else:
                return min(
                    memo(i, j + 1, 0), abs(robot[i] - factory[j][0]) + memo(i + 1, j, curr_robots + 1))

        return memo(0, 0, 0)

    def min_total_distance_dp(self, robot, factory):
        robot.sort()
        factory.sort()
        m = len(robot)
        n = len(factory)
        dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in reversed(range(m + 1)):
            for j in reversed(range(n + 1)):
                for k in range(m + 1):
                    if i >= m:
                        dp[i][j][k] = 0
                    elif j >= n:
                        dp[i][j][k] = math.inf
                    elif k >= factory[j][1]:
                        dp[i][j][k] = dp[i][j + 1][0]
                    else:
                        dp[i][j][k] = min(dp[i][j + 1][0], abs(robot[i] - factory[j][0]) + dp[i + 1][j][k + 1])
        return dp[0][0][0]


s = Solution()
print(s.minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]]))
print(s.minimumTotalDistance([1, -1], [[-2, 1], [2, 1]]))
