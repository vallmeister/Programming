from functools import cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        md = days[-1]
        days = set(days)

        @cache
        def memo(d):
            if d > md:
                return 0
            elif d not in days:
                return memo(d + 1)
            return min(memo(d + 1) + costs[0], memo(d + 7) + costs[1], memo(d + 30) + costs[2])

        dp = [0] * 367
        for i in reversed(range(1, 366)):
            if i not in days:
                dp[i] = dp[i + 1]
            else:
                dp[i] = min(dp[i + 1] + costs[0], dp[min(i + 7, 366)] + costs[1], dp[min(i + 30, 366)] + costs[2])
        return max(dp)
