from functools import cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @cache
        def memoization(day, hold):
            if day >= n:
                return 0
            elif hold:
                return max(memoization(day + 1, True), prices[day] + memoization(day + 2, False))
            else:
                return max(memoization(day + 1, False), -prices[day] + memoization(day + 1, True))

        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n - 1][1] = prices[-1]
        for i in reversed(range(n - 1)):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
            dp[i][1] = max(dp[i + 1][1], dp[i + 2][0] + prices[i])

        return dp[0][0]


s = Solution()
print(s.maxProfit([1, 2, 3, 0, 2]))
print(s.maxProfit([1]))
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit(
    [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11,
     94]))
