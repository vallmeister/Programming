from functools import cache
from typing import List


class Solution:
    # too slow
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def memoization(day, t, hold):
            if day >= n or t == 0:
                return 0
            elif hold:
                return max(memoization(day + 1, t, True), memoization(day + 1, t - 1, False) + prices[day])
            else:
                return max(memoization(day + 1, t, False), memoization(day + 1, t, True) - prices[day])

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in reversed(range(n)):
            for t in range(1, k + 1):
                dp[i][t][0] = max(dp[i + 1][t][0], dp[i + 1][t][1] - prices[i])
                dp[i][t][1] = max(dp[i + 1][t][1], dp[i + 1][t - 1][0] + prices[i])

        return dp[0][k][0]


s = Solution()
print(s.maxProfit(2, [2, 4, 1]))
print(s.maxProfit(2, [3, 2, 6, 5, 0, 3]))
print(s.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
