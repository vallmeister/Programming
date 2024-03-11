from functools import cache


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)

        @cache
        def memoization(day, hold):
            if day >= n:
                return 0
            elif hold:
                return max(memoization(day + 1, True), prices[day] - fee + memoization(day + 1, False))
            else:
                return max(memoization(day + 1, False), memoization(day + 1, True) - prices[day])

        dp = [[0] * 2 for _ in range(n + 1)]
        for i in reversed(range(n)):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
            dp[i][1] = max(dp[i + 1][1], prices[i] - fee + dp[i + 1][0])

        return dp[0][0]


s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
print(s.maxProfit([1, 3, 7, 5, 10, 3], 3))
print(s.maxProfit([7, 1, 5, 3, 6, 4], 1))
print(s.maxProfit([1, 2, 3, 4, 5], 2))
print(s.maxProfit([7, 6, 4, 3, 1], 3))
