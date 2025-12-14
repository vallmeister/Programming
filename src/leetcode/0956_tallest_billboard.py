import math
from functools import cache
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        # @cache
        # def memo(i, diff):
        #     if i >= n:
        #         return 0 if diff == 0 else -math.inf
        #     not_take = memo(i + 1, diff)
        #     take_left = memo(i + 1, diff + rods[i]) + (rods[i] if diff >= 0 else max(0, diff + rods[i]))
        #     take_right = memo(i + 1, diff - rods[i]) + (rods[i] if diff <= 0 else max(0, rods[i] - diff))
        #     return max(not_take, take_left, take_right)

        dp = [[-math.inf] * 10_001 for _ in range(n + 1)]
        dp[n][0] = 0
        for i in reversed(range(n)):
            rod = rods[i]
            for j in range(-5_000, 5_001):
                no_take = dp[i + 1][j]
                take_left = dp[i + 1][j + rod] + (rod if j >= 0 else max(0, j + rod))
                take_right = dp[i + 1][j - rod] + (rod if j <= 0 else max(0, rod - j))
                dp[i][j] = max(no_take, take_left, take_right)

        return dp[0][0]


s = Solution()
print(s.tallestBillboard([1, 2, 3, 6]))
print(s.tallestBillboard(rods=[1, 2, 3, 4, 5, 6]))
print(s.tallestBillboard([1, 2]))
print(s.tallestBillboard([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 50, 50, 50, 150, 150, 150, 100, 100, 100, 123]))
